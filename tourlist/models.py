from django.db import models
from django.conf import settings

class Tourmodel(models.Model):
    location = models.CharField(max_length=100)
    location_code = models.CharField(max_length=5)
    positive = models.TextField()
    negative = models.TextField()
    image = models.ImageField()
    tour_loc = models.TextField()
    def __str__(self):                   #이미지를 문자로 표현함
        return self.location_code