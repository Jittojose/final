from django.db import models
from django import forms

# Create your models here.
class data(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.name


class MyForm(forms.Form):
    username = forms.CharField(max_length=100)
    DOB = forms.DateField()
    age = forms.IntegerField()
    phone = forms.CharField(max_length=100)
    email = forms.EmailField()
    address = forms.CharField(max_length=100)
    department = forms.ChoiceField(choices=[("", "-Select Department-"), ("BCom", "BCom"), ("BBA", "BBA"), ("BA", "BA"), ("Physics", "Physics"), ("Chemistry", "Chemistry"), ("Computer", "Computer"), ("Politics", "Politics"), ("Geography", "Geography"), ("History", "History")])



