import requests
from django.shortcuts import render

def index(request):
    """Anasayfa için şablonu döndürür."""
    return render(request, 'index.html')

def search_flight(request):
    """Uçuş bilgilerini arar ve sonuçları döndürür."""
    flight_id = request.GET.get('flight')  # Uçuş ID parametresi
    if not flight_id:
        return render(request, 'index.html', {'error': 'Flight ID is required!'})

    # Flight API çağrısı
    flight_url = f"https://api.magicapi.dev/api/v1/aedbx/aerodatabox/flights/Number/{flight_id}?withAircraftImage=true&withLocation=false"
    headers = {'x-magicapi-key': 'cm5ppmxs30001js032fsnet77'}
    flight_response = requests.get(flight_url, headers=headers)

    if flight_response.status_code != 200:
        return render(request, 'index.html', {'error': 'Flight not found!'})

    flight_data = flight_response.json()
    if not flight_data:
        return render(request, 'index.html', {'error': 'No data available for this flight!'})

    # Şablon ile sonuçları döndürme
    return render(request, 'search_results.html', {'flight_data': flight_data[0]})
