import requests
from django.shortcuts import render
from django.http import JsonResponse
def search_flight(request):
    flight_query = request.GET.get('flight', '')
    if flight_query:
        # Burada flight_query kullanarak bir işlem yapabilirsiniz
        context = {'flight': flight_query}
        return render(request, 'search_results.html', context)
    else:
        return render(request, 'index.html', {'error': 'No flight provided!'})




def index(request):
    return render(request, 'index.html')

def search_flight(request):
    flight_id = request.GET.get('flight_id')
    if not flight_id:
        return JsonResponse({'error': 'Flight ID is required'}, status=400)

    flight_url = f"https://api.magicapi.dev/api/v1/aedbx/aerodatabox/flights/Number/{flight_id}?withAircraftImage=true&withLocation=false"
    headers = {'x-magicapi-key': 'cm35z0y7q0001l803rkcl3wiu'}

    flight_response = requests.get(flight_url, headers=headers)
    if flight_response.status_code == 204:
        return JsonResponse({'error': 'Flight not found'}, status=404)

    flight_data = flight_response.json()
    if not flight_data:
        return JsonResponse({'error': 'No data available for this flight'}, status=404)

    airport_icao = flight_data[0]['arrival']['airport']['icao']
    airport_url = f"https://api.magicapi.dev/api/v1/aedbx/aerodatabox/airports/Icao/{airport_icao}?withRunways=false&withTime=false"
    airport_response = requests.get(airport_url, headers=headers)

    if airport_response.status_code != 200:
        return JsonResponse({'error': 'Airport data not available'}, status=404)

    return JsonResponse({
        'flight_data': flight_data[0],
        'airport_data': airport_response.json()
    })
