from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Weapon, Category, Country, WeaponType, Rating
from .forms import ReviewForm, RatingForm
from django.db.models import Q


class TypeCountry:
    def get_types(self):
        return WeaponType.objects.all()

    def get_countries(self):
        return Country.objects.all()


class WeaponView(TypeCountry, ListView):
    model = Weapon
    queryset = Weapon.objects.filter(draft=False)
    template_name = 'weapon/weapon_list.html'


class WeaponDetailView(TypeCountry, DetailView):
    model = Weapon
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        weapon = Weapon.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.weapon = weapon
            form.save()
        return redirect(weapon.get_absolute_url())


class CountryView(TypeCountry, DetailView):
    model = Country
    template_name = 'weapon/country.html'
    slug_field = 'url'


class FilterWeaponView(TypeCountry, ListView):
    def get_queryset(self):
        queryset = Weapon.objects.filter(
            Q(country__in=self.request.GET.getlist("country")),
            Q(typeWeapon__in=self.request.GET.getlist("typeWeapon"))
        )
        return queryset


class JsonFilterMoviesView(ListView):
    def get_queryset(self):
        queryset = Weapon.objects.filter(
            Q(country__in=self.request.GET.getlist("country")) |
            Q(typeWeapon__in=self.request.GET.getlist("typeWeapon"))
        ).distinct().values("name", "price", "url", "image")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"weapons": queryset}, safe=False)


class AddStarRating(View):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                weapon_id=int(request.POST.get("weapon")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class Search(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Weapon.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
