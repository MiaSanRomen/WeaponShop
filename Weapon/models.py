from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Bullets(models.Model):
    name = models.CharField("Пули", max_length=150)
    description = models.TextField("Описание")
    price = models.IntegerField("Цена", default=0)
    image = models.ImageField("Изображение", upload_to="bullets/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пули"
        verbose_name_plural = "Пули"


class Country(models.Model):
    name = models.CharField("Страна", max_length=150)
    image = models.ImageField("Флаг", upload_to="flags/")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def get_absolute_url(self):
        return reverse("country_detail", kwargs={"slug": self.url})


class WeaponType(models.Model):
    name = models.CharField("Тип оружия", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="types/")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Weapon(models.Model):
    name = models.CharField("Оружие", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="types/")
    price = models.IntegerField("Цена", default=0)
    url = models.SlugField(max_length=160, unique=True)
    typeWeapon = models.ManyToManyField(WeaponType, verbose_name="типы оружия")
    bullets = models.ManyToManyField(Bullets, verbose_name="пули")
    draft = models.BooleanField("Черновик", default=False)
    country = models.ManyToManyField(Country, verbose_name="страны")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("weapon_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружия"


class RatingStar(models.Model):
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда"
        verbose_name_plural = "Звёзды"
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, verbose_name="оружие")

    def __str__(self):
        return f"{self.star} - {self.weapon}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, verbose_name="оружие")

    def __str__(self):
        return f"{self.name} - {self.weapon}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
