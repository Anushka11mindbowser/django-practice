from rest_framework import serializers
from .models import Person, Toppings, Songs
class ToppingSerializer(serializers.ModelSerializer):
    topping_name = serializers.CharField(max_length=200)
    class Meta:
        model = Toppings
        fields = '__all__'
    def create(self, validated_data):
        return Toppings.objects.create(**validated_data)

class PizzaSerializer(serializers.Serializer):
    pizza_name = serializers.CharField(max_length=200)

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    surname = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=200)
    state = serializers.CharField(max_length=200)
    country = serializers.CharField(max_length=200)

    def person_create(self, validate_data):
        return Person.objects.create(**validate_data)

class SongsSerializer(serializers.Serializer):
    s_id = serializers.CharField(max_length=200)
    s_name = serializers.CharField(max_length=200)
    s_artist = serializers.CharField(max_length=200)
    r_date = serializers.DateField()
    s_genre = serializers.CharField(max_length=200)
    class Meta():
        model = Songs
        fields = '__all__'
    def create(self, validated_data):
        return Songs.objects.create(**validated_data)

