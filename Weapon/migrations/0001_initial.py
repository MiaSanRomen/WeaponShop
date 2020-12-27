# Generated by Django 3.0.5 on 2020-04-20 09:23

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bullets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Пули')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='bullets/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Пули',
                'verbose_name_plural': 'Пули',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Страна')),
                ('image', models.ImageField(upload_to='flags/', verbose_name='Флаг')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда',
                'verbose_name_plural': 'Звёзды',
            },
        ),
        migrations.CreateModel(
            name='WeaponType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Тип оружия')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='types/', verbose_name='Изображение')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Оружие')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='types/', verbose_name='Изображение')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('bullets', models.ManyToManyField(to='weapon.Bullets', verbose_name='пули')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='weapon.Category', verbose_name='Категория')),
                ('country', models.ManyToManyField(to='weapon.Country', verbose_name='страны')),
                ('typeWeapon', models.ManyToManyField(to='weapon.WeaponType', verbose_name='типы оружия')),
            ],
            options={
                'verbose_name': 'Оружие',
                'verbose_name_plural': 'Оружия',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='weapon.Reviews', verbose_name='Родитель')),
                ('weapon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapon.Weapon', verbose_name='оружие')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapon.RatingStar', verbose_name='звезда')),
                ('weapon', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='weapon.Weapon', verbose_name='оружие')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
    ]
