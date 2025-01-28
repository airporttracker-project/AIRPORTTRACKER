// Form validasyonu ve animasyon
const flightForm = document.getElementById('flightForm');
const flightInput = document.getElementById('flight');

// Geçmiş aramalar için bir konteyner oluştur ve sayfaya ekle
const historyContainer = document.createElement("div");
historyContainer.innerHTML = "<h3>Previous Searches:</h3><ul id='searchHistory'></ul>";
document.querySelector(".container").appendChild(historyContainer);

const searchHistoryList = document.getElementById("searchHistory");

// LocalStorage'dan geçmiş aramaları al
function loadSearchHistory() {
    let searches = JSON.parse(localStorage.getItem("flightSearches")) || [];
    searchHistoryList.innerHTML = "";
    searches.forEach(flight => {
        let li = document.createElement("li");
        li.innerHTML = `<a href='/search/?flight=${flight}'>${flight}</a>`;
        searchHistoryList.appendChild(li);
    });
}

// Form gönderildiğinde uçuş ID'sini kaydet
flightForm.addEventListener('submit', function(event) {
    if (flightInput.value.trim() === '') {
        alert('Please enter a valid flight ID.');
        event.preventDefault(); // Formun gönderilmesini engeller
    } else {
        let flightID = flightInput.value.trim().toUpperCase();
        let searches = JSON.parse(localStorage.getItem("flightSearches")) || [];
        if (!searches.includes(flightID)) {
            searches.unshift(flightID); // Yeni aramayı başa ekle
            if (searches.length > 5) searches.pop(); // En fazla 5 arama sakla
            localStorage.setItem("flightSearches", JSON.stringify(searches));
        }
        alert(`Searching for flight: ${flightInput.value}`);
    }
});

// Sayfa yüklendiğinde geçmiş aramaları göster
document.addEventListener("DOMContentLoaded", loadSearchHistory);
