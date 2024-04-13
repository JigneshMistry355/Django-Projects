from django.db import models

# Create your models here.

class Student(models.Model):
    student_rollno = models.IntegerField(unique=True) 
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(unique=True)
    student_city = models.CharField(max_length=50)
    student_percentage = models.FloatField()


    

