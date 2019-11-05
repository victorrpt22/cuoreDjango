from rest_framework import serializers
from hospital.models import Account, Address
from hospital.serializers import AddressSerializer

class AccountSerializer(serializers.ModelSerializer):
    address = AddressSerializer(write_only=True)
    class Meta:
        model = Account
        fields = ('id','password', 'first_name',
                'last_name','username', 'email', 'address','phone_number','gender')

    def create(self, validated_data):
        if 'address' in validated_data.keys():
            address_data = validated_data.pop('address', None)
            address = Address.objects.create(**address_data)
            address.save()
            validated_data['address'] = address
        account = Account.objects.create(**validated_data)
        account.set_password(validated_data['password'])
        account.save()
        return account
