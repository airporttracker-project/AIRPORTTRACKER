from django.urls import path
from AirportTracker import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search-flight/', views.search_flight, name='search_flight'),
]
