from django.db import models
from django.forms import CharField
from django.urls import reverse

# Create your models here.
#models represtns tables here school and student are the tables
class school(models.Model):
    name_of_the_school = models.CharField(max_length=250)
    prinicipal = models.CharField(max_length=100)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('schoolapp:detail',kwargs={'pk':self.pk})

#create one more model with name of student
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(school,related_name='student',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


