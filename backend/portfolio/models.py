from django.db import models
from django.conf import settings
import uuid
import os
from django.utils.timezone import now
from django.db.models.signals import pre_save
from django.dispatch import receiver

def image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4().hex, ext)
    upload_path = os.path.join('uploads', 'image', filename)

    return upload_path


class TagGroup(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'portfolio_tag_group'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=256)
    group = models.ForeignKey(TagGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'portfolio_tag'

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(null=True, upload_to=image_file_path)
    instagram =models.CharField(max_length=128, blank=True, null=True)
    deviant =models.CharField(max_length=128, blank=True, null=True)
    twitter = models.CharField(max_length=128, blank=True, null=True)
    oficial = models.CharField(max_length=128, blank=True, null=True)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-')
        return super().save(*args, **kwargs)


class Art(models.Model):
    TYPE_CHOICES = [
        (1, 'Drawing'),
        (2, 'Painting'),
        (3, 'Sculpture'),
        (4, 'Tatoo'),
        (5, 'Photo'),
        (6, 'Digital')
    ]

    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    description = models.TextField(max_length=512, blank=True)
    image = models.ImageField(null=True, upload_to=image_file_path)
    type = models.IntegerField(choices=TYPE_CHOICES)
    created_at = models.DateField(null=False, default=now)
    tags = models.ManyToManyField(Tag, db_table='portfolio_art_tag')
    characters = models.ManyToManyField('Character', db_table='portfolio_art_character')
    artists = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        db_table = 'portfolio_art'

    def __str__(self):
        return self.title

class Character(models.Model):

    class Sex(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    page_id = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    sex = models.CharField(max_length=1, choices=Sex.choices)
    alive = models.BooleanField()
    first_appearance = models.DateField()

    def __str__(self):
        return self.name

