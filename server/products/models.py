from django.db import models

# Create your models here.

class  Product(models.Model):
    image= models.ImageField(upload_to='uploads/images', null=False, blank=False)
    name= models.CharField(max_length=200, null=False, blank=False)
    price= models.DecimalField(max_digits=7, decimal_places=2)
    email= models.EmailField(max_length=200, null=False, blank=False)
    date= models.DateTimeField(auto_now_add=True)
    desciption= models.TextField()
    category= models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
       
