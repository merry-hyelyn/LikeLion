from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    admission_year = models.IntegerField()
    student_number = models.IntegerField()
    level = models.IntegerField()
    grade_avg = models.FloatField()
