from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "image_tag", "photo"]


admin.site.register(Image, ImageAdmin)
