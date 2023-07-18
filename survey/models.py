from django.db import models

# Create your models here.

class Survey(models.Model):
    GENDER_CHOICES = (
        ('M', '남'),
        ('F', '여'),
    )

    AGE_CHOICES = (
        ('1', '10대'),
        ('2', '20대'),
        ('3', '30대'),
        ('4', '40대'),
        ('5', '50대'),
        ('6', '60대 이상'),
    )

    REGION_CHOICES = (
        ('서울특별시', '서울특별시'),
        ('경기도', '경기도'),
        ('인천광역시', '인천광역시'),
        ('강원도', '강원도'),
    )

    AREA_CHOICES = (
        ('강남구', '강남구'),
        ('성동구', '성동구'),
        ('종로구', '종로구'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.CharField(max_length=1,choices=AGE_CHOICES)
    region_1 = models.CharField(max_length=30, choices=REGION_CHOICES)
    area_1 = models.CharField(max_length=30, choices=AREA_CHOICES)
    region_2 = models.CharField(max_length=30, choices=REGION_CHOICES, blank=True)
    area_2 = models.CharField(max_length=30, choices=AREA_CHOICES, blank=True)
    region_3 = models.CharField(max_length=30, choices=REGION_CHOICES, blank=True)
    area_3 = models.CharField(max_length=30, choices=AREA_CHOICES, blank=True)    

   
    myarea_1 = models.CharField(max_length=60)
    myarea_2 = models.CharField(max_length=60, blank=True)
    myarea_3 = models.CharField(max_length=60, blank=True)

    
    def regionsave(self, *args, **kwargs):
        self.myarea_1 = self.region_1 + ' ' + self.area_1
        self.myarea_2 = self.region_2 + ' ' + self.area_2
        self.myarea_3 = self.region_3 + ' ' + self.area_3
