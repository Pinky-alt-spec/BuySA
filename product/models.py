from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

# Create your models here.


class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    keyword = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class MPTTMeta:
        order_insertion_by = ['title']
    
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])
    
class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    AVAILABILITY = (
        ('In Stock', 'In Stock'),
        ('Out Of Stock', 'Out Of Stock'),
    )
    CONDITION = (
        ('New', 'New'),
        ('Hot', 'Hot'),
        ('Sale', 'Sale'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keyword = models.CharField(max_length=30)
    description = RichTextUploadingField(blank=True, null=True)
    information = RichTextUploadingField(blank=True, null=True)
    small_product_details = RichTextUploadingField(blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    minamount = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    availability = models.CharField(max_length=15, choices=AVAILABILITY)
    condition = models.CharField(max_length=10, choices=CONDITION)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def image_tag(self):
            if self.image_tag:
                return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
            return ''

    image_tag.short_description = 'Image'
    

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
