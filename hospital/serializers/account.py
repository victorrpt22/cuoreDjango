from rest_framework import serializers
from hospital.models import Account, Address
from hospital.serializers import AddressSerializer

class AccountSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=True)

    class Meta:
        model = Account
        fields = ('address', 'password', 'first_name',
                'last_name','username', 'email')

    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        address = Address.objects.create(**address_data)
        validated_data['address'] = address
        account = Account.objects.create(**validated_data)
        account.set_password(validated_data['password'])
        account.save()
        return account
