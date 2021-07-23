from django.contrib import admin

# Register your models here.
from blog import models

admin.site.register(models.Region)
admin.site.register(models.UploadedImage)
admin.site.register(models.Category)
admin.site.register(models.Post)