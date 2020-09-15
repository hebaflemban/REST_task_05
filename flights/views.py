from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from datetime import datetime
from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, BookingDetailsSerializer, UpdateBookingSerializer, RegisterSerializer, BasicUpdateSerializer
from .permissions import is_THEauthenticated, CanUpdate

class FlightsList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class BookingsList(ListAPIView):
    serializer_class = BookingSerializer
    def get_queryset(self):
        queryset = Booking.objects.filter(date__gte=datetime.today(), user = self.request.user)
        return queryset

class BookingDetails(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'


class UpdateBooking(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return UpdateBookingSerializer
        elif CanUpdate:
            return BasicUpdateSerializer


class CancelBooking(DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'


class BookFlight(CreateAPIView):
    serializer_class = UpdateBookingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, flight_id=self.kwargs['flight_id'])


class Register(CreateAPIView):
    serializer_class = RegisterSerializer
