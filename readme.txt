# Airport Tracker

The **Airport Tracker** project is a web application designed to track and display real-time flight information for specific airports. It leverages the OpenSky API to provide details about arrivals, departures, and other flight data.

---

## Features

- **Track Real-Time Flights**:
  - View incoming and outgoing flights for specific airports.
  - Fetches flight data dynamically using the OpenSky API.

- **Search and Filter**:
  - Filter flights based on airport codes (e.g., Wrocław Airport's ICAO code `EPWR`).

- **User-Friendly Interface**:
  - A simple, responsive design for easy navigation and flight tracking.

---

## Requirements

- Python 3.9+
- Django 4.2+
- `requests` library for API integration

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/airporttracker-project/AIRPORTTRACKER.git
   cd AIRPORTTRACKER


python -m venv env
source env/bin/activate   # On Linux/macOS
env\\Scripts\\activate    # On Windows

python manage.py migrate


python manage.py runserver



Bir hata oluştu, ancak README dosyasını tekrar oluşturup size indirilebilir hale getireceğim. Lütfen bekleyin. ​​

README dosyasını bir metin dosyası olarak başarıyla oluşturdum, ancak indirilebilir hale getirme sırasında bir hata oluştu. Size dosyayı manuel olarak sağlayabilmem için içeriği buraya yapıştırıyorum.

Aşağıdaki içeriği bir dosyaya kaydedebilirsiniz (örneğin, README.txt):

txt
Copy
Edit
# Airport Tracker

The **Airport Tracker** project is a web application designed to track and display real-time flight information for specific airports. It leverages the OpenSky API to provide details about arrivals, departures, and other flight data.

---

## Features

- **Track Real-Time Flights**:
  - View incoming and outgoing flights for specific airports.
  - Fetches flight data dynamically using the OpenSky API.

- **Search and Filter**:
  - Filter flights based on airport codes (e.g., Wrocław Airport's ICAO code `EPWR`).

- **User-Friendly Interface**:
  - A simple, responsive design for easy navigation and flight tracking.

---

## Requirements

- Python 3.9+
- Django 4.2+
- `requests` library for API integration

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/airporttracker-project/AIRPORTTRACKER.git
   cd AIRPORTTRACKER
Create a Virtual Environment (Optional but Recommended):

bash
Copy
Edit
python -m venv env
source env/bin/activate   # On Linux/macOS
env\\Scripts\\activate    # On Windows
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply Database Migrations:

bash
Copy
Edit
python manage.py migrate
Run the Development Server:

bash
Copy
Edit
python manage.py runserver
Usage
Open your web browser and navigate to:

Arrivals: http://127.0.0.1:8000/arrivals/
Departures: http://127.0.0.1:8000/departures/
The application will fetch real-time flight data for Wrocław Airport (EPWR).


