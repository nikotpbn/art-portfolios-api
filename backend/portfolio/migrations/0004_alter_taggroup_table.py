# Generated by Django 4.1.2 on 2022-11-09 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_taggroup_alter_tag_group'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='taggroup',
            table='portfolio_tag_group',
        ),
    ]