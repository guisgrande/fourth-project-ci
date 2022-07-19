from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Car(models.Model):
    """
    Class to represent Car database model
    """
    car_id = models.SmallAutoField(primary_key=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='car_post')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.FloatField(max_length=11)
    hp = models.FloatField(max_length=4)
    speed = models.FloatField(max_length=6)
    description = models.TextField(max_length=500, null=True)
    car_image = CloudinaryField('image', default='placeholder')
    favorite = models.ManyToManyField(
        User, related_name='favorite_car',
        blank=True)
    slug = models.SlugField(unique=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Class to show newest car first 
        """
        ordering = ['-created_on']

    def __str__(self):
        return str(self.car_id)

    def save(self, *args, **kwargs):
        """
        Function to auto generate slugfield
        """
        autoslug = self.brand + '-' + self.model + '-' + str(self.year)
        self.slug = slugify(autoslug)
        super(Car, self).save(*args, **kwargs)

    def number_of_favorites(self):
        """
        Function to count number of favorites
        """
        return self.favorite.count()