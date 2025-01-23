import requests
from django.shortcuts import render
from datetime import datetime, timezone

def index(request):
    """Anasayfa için şablonu döndürür."""
    return render(request, 'index.html')

def search_flight(request):
    """CallSign'e göre uçuş bilgilerini arar ve sonuçları döndürür."""
    flight_callsign = request.GET.get('flight')
    if not flight_callsign:
        return render(request, 'index.html', {'error': 'Flight CallSign is required!'})

    # Aerodatabox API isteği
    flight_url = (
        f"https://api.magicapi.dev/api/v1/aedbx/aerodatabox/flights/CallSign/"
        f"{flight_callsign}?withAircraftImage=false&withLocation=false"
    )
    headers = {'x-magicapi-key': 'cm5ppmxs30001js032fsnet77'}
    response = requests.get(flight_url, headers=headers)

    if response.status_code != 200:
        return render(request, 'index.html', {'error': 'Flight not found!'})

    flights = response.json()
    if not flights:
        return render(request, 'index.html', {'error': 'No data available for this flight!'})

    STATUS_MAP = {
        'EnRoute': 'On the Way'
        # Gerekirse başka durumlar ekleyin
    }

    for flight in flights:
        # Status dönüştürme
        raw_status = flight.get('status', 'Unknown')
        flight['status'] = STATUS_MAP.get(raw_status, raw_status)

        # Zaman formatlama (timezone offset kaldırma)
        dep_local_str = flight.get('departure', {}).get('scheduledTime', {}).get('local')
        arr_local_str = (
            flight.get('arrival', {}).get('scheduledTime', {}).get('local')
            or flight.get('arrival', {}).get('predictedTime', {}).get('local')
        )
        if dep_local_str:
            dep_dt = datetime.fromisoformat(dep_local_str.replace('Z', '+00:00'))
            flight['departure']['scheduledTime']['local'] = dep_dt.strftime('%Y-%m-%d %H:%M')
        if arr_local_str:
            arr_dt = datetime.fromisoformat(arr_local_str.replace('Z', '+00:00'))
            if 'scheduledTime' in flight['arrival'] and 'local' in flight['arrival']['scheduledTime']:
                flight['arrival']['scheduledTime']['local'] = arr_dt.strftime('%Y-%m-%d %H:%M')
            elif 'predictedTime' in flight['arrival'] and 'local' in flight['arrival']['predictedTime']:
                flight['arrival']['predictedTime']['local'] = arr_dt.strftime('%Y-%m-%d %H:%M')

        # Uçuşun yüzde kaçının tamamlandığını hesapla + kalan süre
        try:
            now_utc = datetime.now(timezone.utc)
            dep_for_calc = datetime.fromisoformat(dep_local_str.replace('Z', '+00:00'))
            arr_for_calc = datetime.fromisoformat(arr_local_str.replace('Z', '+00:00'))

            total_duration = (arr_for_calc - dep_for_calc).total_seconds()
            elapsed = (now_utc - dep_for_calc).total_seconds()
            remaining = (arr_for_calc - now_utc).total_seconds()

            # Tamamlanma yüzdesi
            percentage = 0
            if total_duration > 0:
                ratio = elapsed / total_duration
                if ratio < 0:
                    percentage = 0
                elif ratio > 1:
                    percentage = 100
                else:
                    percentage = int(ratio * 100)
            flight['completionPercent'] = percentage

            # Kalan süre (basit saat:dakika formatı)
            if remaining > 0:
                hours = int(remaining // 3600)
                minutes = int((remaining % 3600) // 60)
                flight['timeRemaining'] = f"{hours}h {minutes}m"
            else:
                flight['timeRemaining'] = "0h 0m"
        except:
            flight['completionPercent'] = 0
            flight['timeRemaining'] = "Unknown"

    return render(request, 'search_results.html', {'flights': flights})
