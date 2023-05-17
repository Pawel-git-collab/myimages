from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images')
    image_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(200, 200)],
                                     format='JPEG',
                                     options={'quality': 60})

    image_thumbnail2 = ImageSpecField(source='photo',
                                      processors=[ResizeToFill(400, 400)],
                                      format='JPEG',
                                      options={'quality': 60})

    def image_tag(self):
        return self.photo
