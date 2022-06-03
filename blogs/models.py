from django.db import models

# Create your models here.

class Songs(models.Model):
    s_id = models.IntegerField()
    s_name = models.CharField(max_length=200)
    s_artist = models.CharField(max_length=200)
    r_date = models.DateField()
    s_genre = models.CharField(max_length=200)

class Toppings(models.Model):
    topping_name = models.CharField(max_length=200)
    def __str__(self):
        return self.topping_name

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    topping_name = models.ForeignKey(Toppings, on_delete=models.CASCADE)
    def __str__(self):
       return self.pizza_name


class Artist(models.Model):
    artist_name = models.CharField(max_length=200)

class Band(models.Model):
    band_name = models.CharField(max_length=200)
    artist_name = models.ManyToManyField(Artist, through='Membership')

class Membership(models.Model):
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    band_name = models.ForeignKey(Band, on_delete=models.CASCADE)
    doj = models.DateField()
    comment = models.CharField(max_length=200)

class Demo(models.Model):
    demo_field = models.CharField(max_length=200)

class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

class Movies(models.Model):
    m_id = models.CharField(max_length=200)
    m_name = models.CharField(max_length=200)
    m_director = models.CharField(max_length=200)
    m_rd = models.DateField()
    m_genre = models.CharField(max_length=200)


class FoodItems(models.Model):
    f_id = models.CharField(max_length=200)
    f_name = models.CharField(max_length=200)

class Books(models.Model):
    b_id = models.CharField(max_length=200)
    b_name = models.CharField(max_length=200)
    b_author = models.CharField(max_length=200)
    b_genre = models.CharField(max_length=200)

