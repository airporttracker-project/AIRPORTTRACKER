// Form validasyonu ve animasyon
document.getElementById('flightForm').addEventListener('submit', function(event) {
    const flightInput = document.getElementById('flight');
    if (flightInput.value.trim() === '') {
        alert('Please enter a valid flight ID.');
        event.preventDefault(); // Formun gönderilmesini engeller
    } else {
        alert(`Searching for flight: ${flightInput.value}`);
    }
});