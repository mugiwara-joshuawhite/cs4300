from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db import IntegrityError, transaction

# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.response import Response

# Models
from .models import Movie, Booking, Seat

# Serializers
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    '''
    For CRUD operations on movies
    '''
    # For API endpoints
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def movie_list(request):
        movie_list = Movie.objects.all()
        movies = {"movies": movie_list}
        return render(request, "bookings/movie_list.html", movies)

class SeatViewSet(viewsets.ModelViewSet):
    '''
    For seat availability and booking
    '''

    # For API endpoints
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    def seat_booking(request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)

        if request.method == "POST":
            seat = get_object_or_404(Seat, pk=request.POST.get("seat_id"))
            user = request.POST.get("user", "").strip()

            if not user:
                return HttpResponseBadRequest("Enter your name.")
            try:
                with transaction.atomic():
                    Booking.objects.create(
                        movie=movie,
                        seat=seat,
                        user=user,
                        booking_date=timezone.localdate(),
                    )
            except IntegrityError:
                return HttpResponseBadRequest("That seat is already booked for this movie.")
            return redirect("booking_history")

        seats = list(Seat.objects.order_by("seat_number"))
        booked_seat_ids = set(
            Booking.objects.filter(movie=movie, seat__isnull=False)
            .values_list("seat_id", flat=True)
        )
        for seat in seats:
            seat.is_booked = seat.pk in booked_seat_ids
        rows = [seats[i:i+8] for i in range(0, len(seats), 8)]
        return render(request, "bookings/seat_booking.html", {"movie": movie, "rows": rows})

class BookingViewSet(viewsets.ModelViewSet):
    '''
    For users to book seats and view their booking history
    '''

    # For API endpoints
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def booking_history(request):
        return render(request, "bookings/booking_history.html", {"bookings": Booking.objects.all()})

# Automatically redirect to movie list page upon loading
def home(request):
    return redirect('movie_list')