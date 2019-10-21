from rest_framework import serializers
from hospital.models import Address, Account

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'
