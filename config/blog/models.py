from django.db import models
from django.conf import settings
# Create your models here.


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='%Y/%m/%d')

    class Meta:
        managed = True
        db_table = 'upload_images'

    def __str__(self):
        return self.image.name


class Region(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'regions'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=800)
    image = models.ForeignKey(UploadedImage, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'posts'

    def __str__(self):
        return self.name