from django.contrib import admin
from .models import Category, Bullets, Country, WeaponType, Weapon, Reviews, RatingStar, Rating
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInLine(admin.StackedInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "url", "draft")
    search_fields = ("name", "category__name")
    inlines = [ReviewInLine]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "weapon", "id")
    readonly_fields = ("name", "email")


@admin.register(Bullets)
class BulletsAdmin(TranslationAdmin):
    list_display = ("id", "name")


@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    list_display = ("name", "url")


@admin.register(WeaponType)
class WeaponTypeAdmin(TranslationAdmin):
    list_display = ("name", "url")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "weapon", "ip")


admin.site.register(RatingStar)

admin.site.site_title = "Weapon shop"
admin.site.site_header = "Weapon shop"
