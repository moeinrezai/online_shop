from django.db import models



class Size(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title



class Colors(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title



# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to="products")
    size = models.ManyToManyField(Size, blank=True, null=True, related_name="products")
    color = models.ManyToManyField(Colors, blank=True, null=True, related_name="products")

    def __str__(self):
        return self.title