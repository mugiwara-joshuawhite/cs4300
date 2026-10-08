from django.db import IntegrityError, transaction
from django.test import TestCase

from .models import Booking, Movie, Seat


class MovieTests(TestCase):
    def test_movie_model(self):
        movie = Movie.objects.create(
            title="Test Movie",
            description="This is a test movie.",
            release_date="2023-01-01",
            duration=120,
        )

        self.assertEqual(movie.title, "Test Movie")
        self.assertEqual(movie.description, "This is a test movie.")
        self.assertEqual(str(movie.release_date), "2023-01-01")
        self.assertEqual(movie.duration, 120)

    def test_seat_model(self):
        seat = Seat.objects.create(seat_number=1, booking_status=False)

        self.assertEqual(seat.seat_number, 1)
        self.assertFalse(seat.booking_status)

    def test_booking_model(self):
        movie = Movie.objects.create(
            title="Test Movie",
            description="This is a test movie.",
            release_date="2023-01-01",
            duration=120,
        )
        seat = Seat.objects.create(seat_number=1, booking_status=False)
        booking = Booking.objects.create(
            movie=movie,
            seat=seat,
            user="Test User",
            booking_date="2023-01-01",
        )

        self.assertEqual(booking.movie, movie)
        self.assertEqual(booking.seat, seat)
        self.assertEqual(booking.user, "Test User")
        self.assertEqual(str(booking.booking_date), "2023-01-01")

    def test_booking_unique_constraint(self):
        movie = Movie.objects.create(
            title="Test Movie",
            description="This is a test movie.",
            release_date="2023-01-01",
            duration=120,
        )
        seat = Seat.objects.create(seat_number=1, booking_status=False)
        Booking.objects.create(
            movie=movie,
            seat=seat,
            user="Test User",
            booking_date="2023-01-01",
        )

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Booking.objects.create(
                    movie=movie,
                    seat=seat,
                    user="Another User",
                    booking_date="2023-01-02",
                )

    def test_seat_booking_status_update(self):
        seat = Seat.objects.create(seat_number=1, booking_status=False)
        seat.booking_status = True
        seat.save()

        updated_seat = Seat.objects.get(id=seat.id)

        self.assertTrue(updated_seat.booking_status)