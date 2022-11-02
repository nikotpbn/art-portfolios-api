from django.db import models
from django.conf import settings
import uuid
import os
from django.utils.timezone import now

def image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4().hex, ext)
    upload_path = os.path.join('uploads', 'image', filename)

    return upload_path

class Art(models.Model):
    Options = [
        (1, 'Drawing'),
        (2, 'Painting'),
        (3, 'Sculpture'),
        (4, 'Tatoo'),
        (5, 'Photo'),
        (6, 'Digital')
    ]

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256, null=False)
    subtitle = models.CharField(max_length=256, null=True)
    description = models.TextField(max_length=512, null=True)
    image = models.FileField(upload_to=image_file_path)
    type = models.IntegerField(choices=Options, null=False)
    created_at = models.DateField(null=False, default=now)

    class Meta:
        db_table = 'portfolio_art'