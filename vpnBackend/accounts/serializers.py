from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from django.db import transaction
from .models import (Clients,Wallet,incrementRequest,decrementRequest,admins)
from django.contrib.auth.password_validation import validate_password

class clientSerializer(ModelSerializer):
    class Meta:
        model=Clients
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'is_blocked', 
            'img',
            'date_joined'
        ]




class walletSerializer(ModelSerializer):
    client=serializers.StringRelatedField(many=False)
    class Meta:
        model=Wallet
        fields=['id','client','balance','createdDate']
        extra_kwargs = {
            'id': {'read_only' : True},
            'client': {'read_only' : True},
            'balance': {'read_only' : True},
            'createdDate': {'read_only' : True}
        }



class incrementRequestSerializer(ModelSerializer):
    wallet=serializers.PrimaryKeyRelatedField()
    class Meta:
        model=incrementRequest
        fields='__all__'
        read_only_fields = ['id','date','wallet','amount']




class decrementRequestSerializer(ModelSerializer):
    wallet=serializers.PrimaryKeyRelatedField()
    class Meta:
        model=decrementRequest
        fields='__all__'
        read_only_fields=['id','date','wallet','amount','']


class adminSerializer(ModelSerializer):
    class Meta:
        model=admins
        fields='__all__'




class EmailSerializer(serializers.Serializer):
    email=serializers.EmailField()


class confirmEmailSerializer(serializers.Serializer):
    email=serializers.EmailField()
    token=serializers.CharField()


class confirmPasswordSerializer(serializers.Serializer):
    email=serializers.EmailField()
    token=serializers.CharField()
    new_password=serializers.CharField()



class clientRegisterSerializer(ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True, required=True)
    class Meta:
        model=Clients
        fields=[ 
            'username', 
            'email', 
            'first_name', 
            'last_name',
            'password',
            'password_confirm'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise ValidationError({"password": "Passwords do not match."})
        return attrs
    
    @transaction.atomic
    def create(self, validated_data):
        validated_data.pop('password_confirm',None)
        client=Clients.objects.create(**validated_data)
        return client
        
