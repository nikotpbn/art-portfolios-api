# Generated by Django 4.1.2 on 2023-02-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_artist_twitter_alter_artist_deviant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='oficial',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]