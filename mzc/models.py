from django.db import models

# Create your models here.
GENDER_CHOICE=(
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHERS')
)
class Students(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=30)
    address=models.TextField()
    course=models.CharField(max_length=40)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICE,default='M')

class Faculty(models.Model):
    name=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    address=models.TextField()
    subject=models.CharField(max_length=30)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICE,default='M')
