from rest_framework import serializers
from .models import Property , User


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Assuming the seller is a User model
        fields = ['id', 'username', 'email', 'phone_number', 'first_name', 'last_name',]  # Add more fields as needed

class PropertyCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'place', 'area', 'number_of_bedrooms', 'number_of_bathrooms', 'nearby_hospitals', 'nearby_colleges', 'description', 'price']
        read_only_fields = ['id']

class PropertyListSerializer(serializers.ModelSerializer):
    seller = SellerSerializer()  # Nested serializer for seller details
    class Meta:
        model = Property
        fields = ['id', 'place', 'area', 'number_of_bedrooms', 'number_of_bathrooms', 'nearby_hospitals', 'nearby_colleges', 'description','price', 'seller']

class PropertyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'place', 'area', 'number_of_bedrooms', 'number_of_bathrooms', 'nearby_hospitals', 'nearby_colleges', 'description', 'price', 'seller', 'created_at', 'updated_at']

