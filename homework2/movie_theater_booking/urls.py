"""
URL configuration for movie_theater_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookings import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('movie-list', views.MovieViewSet.movie_list, name='movie_list'),
    path('book-seat/<int:movie_id>/', views.SeatViewSet.seat_booking, name='book_seat'),
    path('booking-history', views.BookingViewSet.booking_history, name='booking_history'),

    # API endpoints
    path('api/movies/', views.MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_movies'),
    path('api/seats/', views.SeatViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_seats'),
    path('api/bookings/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_bookings'),
]
