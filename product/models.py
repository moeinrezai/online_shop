from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name="subs")
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title


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
    category = models.ManyToManyField(Category, blank=True, null=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="products")
    size = models.ManyToManyField(Size, blank=True, null=True, related_name="products")
    color = models.ManyToManyField(Colors, blank=True, null=True, related_name="products")

    def __str__(self):
        return self.title



class Information(models.Model):
    product = models.ForeignKey(Product,null=True, blank=True, on_delete=models.CASCADE, related_name="information")
    text = models.TextField()

    def __str__(self):
        return self.text[:50]