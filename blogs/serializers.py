from rest_framework import serializers
from .models import Person, Toppings, Songs, Movies, FoodItems, Books, Flowers

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


class MovieSerializer(serializers.Serializer):
    m_id = serializers.CharField(max_length=200)
    m_name = serializers.CharField(max_length=200)
    m_director = serializers.CharField(max_length=200)
    m_rd = serializers.DateField()
    m_genre = serializers.CharField(max_length=200)
    class Meta():
        model = Movies
        fields ='__all__'

    def create(self, validated_data):
        return Movies.objects.create(**validated_data)


class FoodItemsSerializer(serializers.Serializer):
    f_id = serializers.CharField(max_length=200)
    f_name = serializers.CharField(max_length=200)
    class Meta():
        model = FoodItems
        fields = '__all__'

    def create(self, validated_data):
        return FoodItems.objects.create(**validated_data)

class BookSeializer(serializers.Serializer):
    b_id = serializers.CharField(max_length=200)
    b_name = serializers.CharField(max_length=200)
    b_author = serializers.CharField(max_length=200)
    b_genre = serializers.CharField(max_length=200)

    class Meta():
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        return Books.objects.create(**validated_data)

class FlowerSerializer(serializers.Serializer):
    f_id = serializers.CharField(max_length=200)
    f_name = serializers.CharField(max_length=200)

    class Meta():
        model = Flowers
        fields = '__all__'

    def create(self, validated_data):
        return Flowers.objects.create(**validated_data)