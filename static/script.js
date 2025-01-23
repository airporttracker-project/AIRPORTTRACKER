document.addEventListener('DOMContentLoaded', function() {
    // 1) Uçuş kartlarına basit bir fade-in efekti ekleyelim:
    const flightCards = document.querySelectorAll('.flight-card');
    flightCards.forEach((card, index) => {
        // Başlangıç değerleri (gizli, aşağıda hafif kayık)
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';

        // Kartları sırayla görünür yapmak için zamanlayıcı
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 150); // her kart için 150ms gecikme
    });

    // 2) Tamamlanma barını (ilk uçuşun verileri) da benzer şekilde animasyonla göstermek:
    const completionBarContainer = document.querySelector('.completion-bar-container');
    if (completionBarContainer) {
        // Başlangıç değerleri
        completionBarContainer.style.opacity = '0';
        completionBarContainer.style.transform = 'translateY(20px)';
        completionBarContainer.style.transition = 'opacity 0.5s ease, transform 0.5s ease';

        // Kartların ardından devreye girecek şekilde kısa gecikme
        setTimeout(() => {
            completionBarContainer.style.opacity = '1';
            completionBarContainer.style.transform = 'translateY(0)';
        }, flightCards.length * 150);
    }

    // 3) Eğer form doğrulama veya başka bir etkileşim varsa (örneğin 'flightForm' ID’li form),
    //    onu da burada yönetebilirsiniz:
    const flightForm = document.getElementById('flightForm');
    if (flightForm) {
        flightForm.addEventListener('submit', function(event) {
            const flightInput = document.getElementById('flight');
            if (!flightInput.value.trim()) {
                alert('Please enter a valid flight ID');
                event.preventDefault();
            } else {
                alert('Searching for flight: ' + flightInput.value);
            }
        });
    }
});
