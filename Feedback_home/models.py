from django.db import models

# Create your models here.
class Faculty(models.Model):
    Id_Number=models.IntegerField(primary_key=True)
    Faculty_Name=models.CharField(max_length=100)
    Email_Id=models.EmailField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
class Student(models.Model):
    Id_Number=models.IntegerField(primary_key=True)
    Student_Name=models.CharField(max_length=100)
    Batch_year=models.CharField(max_length=100)
    Branch=models.CharField(max_length=100)
    Email_Id=models.EmailField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
class Feedback(models.Model):
    Feedback_ID=models.IntegerField(primary_key=True)
    Sundaram=models.CharField(max_length=100)
    Rejina = models.CharField(max_length=100)
    Kiranmai = models.CharField(max_length=100)
    Shilpa = models.CharField(max_length=100)
    College_feedback_review=models.CharField(max_length=2000)




