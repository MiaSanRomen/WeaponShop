from modeltranslation.translator import register, TranslationOptions
from .models import Category, Country, WeaponType, Bullets


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Country)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(WeaponType)
class MovieTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Bullets)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
