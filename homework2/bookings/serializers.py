from rest_framework import serializers

# Where I read about all this: https://www.django-rest-framework.org/api-guide/serializers/
class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=256)
    release_date = serializers.DateField()
    duration = serializers.IntegerField()

    # For CRUD operations
    def create(self, validated_data):
        return Movie(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.release_date = validated_data.get("release_date", instance.release_date)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance

class SeatSerializer(serializers.Serializer):
    seat_number = serializers.IntegerField()
    booking_status = serializers.BooleanField(default=False)

    # Allow booking of seats
    def update(self, instance, validated_data):
        instance.booking_status = validated_data.get("booking_status", instance.booking_status)
        instance.save()
        return instance

class BookingSerializer(serializers.Serializer):
    movie = MovieSerializer()
    seat = SeatSerializer()
    user = serializers.CharField(max_length=100)
    booking_date = serializers.DateField()

    # Allow creation of new booking
    def create(self, validated_data):
        movie_data = validated_data.pop("movie")
        seat_data = validated_data.pop("seat")
        movie = Movie.objects.get(title=movie_data["title"])
        seat = Seat.objects.get(seat_number=seat_data["seat_number"])
        booking = Booking.objects.create(movie=movie, seat=seat, **validated_data)
        return booking