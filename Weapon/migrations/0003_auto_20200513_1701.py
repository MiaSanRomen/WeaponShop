# Generated by Django 3.0.5 on 2020-05-13 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weapon', '0002_auto_20200420_1238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда', 'verbose_name_plural': 'Звёзды'},
        ),
    ]
