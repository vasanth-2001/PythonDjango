from django.db import models

# Create your models here.
class Chef(models.Model):
    full_name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=50)

    def __str__(self):
        return f'Name {self.full_name} {self.add} age: {self.age} '
class Dish(models.Model):
    name=models.CharField(max_length=20)
    rating=models.IntegerField()
    is_billing=models.BooleanField()
    price=models.IntegerField()
    chef=models.ForeignKey('Chef',on_delete=models.CASCADE)

