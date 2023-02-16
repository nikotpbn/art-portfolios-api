from django.contrib import admin
from portfolio import models


class TagFilter(admin.FieldListFilter):
    pass


# Register your models here.
admin.site.register(models.Art)
admin.site.register(models.Tag)
admin.site.register(models.TagGroup)
admin.site.register(models.Artist)
admin.site.register(models.Character)