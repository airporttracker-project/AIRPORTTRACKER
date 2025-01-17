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


Usage
Open your web browser and navigate to:

Arrivals: http://127.0.0.1:8000/arrivals/
Departures: http://127.0.0.1:8000/departures/
The application will fetch real-time flight data for Wrocław Airport (EPWR).


Notes
Customizing Airport: Update the AIRPORT_ICAO variable in tracker/views.py to track flights for a different airport.
Production: Set DEBUG = False in settings.py and configure ALLOWED_HOSTS.
