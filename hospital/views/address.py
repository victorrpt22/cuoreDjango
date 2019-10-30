from rest_framework import generics
from hospital.models import Address
from hospital.serializers import AddressSerializer

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
