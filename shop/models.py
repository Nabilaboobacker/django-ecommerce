from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.category
    
    

class Product(models.Model):
    product = models.CharField(max_length=200, unique=True)
    product_slug = models.SlugField(max_length=250, unique=True, blank=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()
    featured_image = models.ImageField(upload_to='images')
    product_description = models.TextField()
    is_new_arrival = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product
