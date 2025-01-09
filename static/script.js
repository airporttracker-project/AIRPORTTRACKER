document.getElementById('search-btn').addEventListener('click', async () => {
    const searchInput = document.getElementById('search-input').value;
    if (!searchInput) return;

    document.getElementById('loading').style.display = 'block';
    document.getElementById('flight-data').style.display = 'none';

    const response = await fetch(`/search-flight/?flight_id=${searchInput}`);
    if (!response.ok) {
        alert('Error fetching flight data.');
        document.getElementById('loading').style.display = 'none';
        return;
    }

    const data = await response.json();
    document.getElementById('aircraft-img').src = data.flight_data.aircraft.image.url;
    document.getElementById('aircraft-name').innerHTML = data.flight_data.aircraft.model;
    document.getElementById('airport-name').innerHTML = data.airport_data.shortName;
    document.getElementById('city-name').innerHTML = data.airport_data.municipalityName;
    document.getElementById('airport-icao').innerHTML = data.airport_data.icao;
    document.getElementById('aiport-iata').innerHTML = data.airport_data.iata;
    document.getElementById('airport-timezone').innerHTML = data.airport_data.timeZone;
    document.getElementById('map-widget').src = `https://www.google.com/maps/embed/v1/place?key=YOUR_GOOGLE_MAPS_API_KEY&q=${data.airport_data.fullName}&zoom=14&language=en`;

    document.getElementById('loading').style.display = 'none';
    document.getElementById('flight-data').style.display = 'block';
});
