from django.db import models

from rest_framework import serializers

# Create your models here.
'''
model Movie - represents a single movie.
title - string for movie title
description - string for paragraph of description
release_date - date of initial screening
duration - int for length of movie in minutes
'''
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    release_date = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title
    
    def url_form(self):
        return self.title.replace(" ", "-")

'''
model Seat - represents a seat in a theater.
seat_number - int for seat label
booking_status - bool for if is booked or not
'''
class Seat(models.Model):
    seat_number = models.IntegerField()
    booking_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.seat_number)

'''
model Booking - represents a reserved ticket for a 
movie in a theater.

movie - OneToOne for one movie per ticket. on_delete 
is SET_NULL as if the movie is deleted, the booking 
should be able to detect that and be able to stick 
around long enough to issue refund.

seat - OneToOne for one seat per ticket. on_delete
is SET_NULL as if the seat is deleted (say it's out
of order), the bookoing should be able to detect that
and be able to stick around long enough to issue
refund or switch seats.

user - string as I'm not sure if we must make
a proper user so I'm just setting it to a name for
now.

booking_date - when the ticket was booked.
'''
class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.SET_NULL, related_name = "movie", null=True)
    seat = models.ForeignKey(Seat, on_delete = models.SET_NULL, related_name = "seatnum", null=True)
    user = models.CharField(max_length=100)
    booking_date = models.DateField()

    # Code suggested by DevEDU chat. I understand what it is doing.
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("movie", "seat"), name="unique_movie_seat_booking"),
        ]

    def __str__(self):
        return f"Booking for {self.user} made on {self.booking_date}"