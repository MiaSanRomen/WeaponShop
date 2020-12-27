from django.urls import path
from . import views


urlpatterns = [
    path("", views.WeaponView.as_view()),
    path("filter/", views.FilterWeaponView.as_view(), name="filter"),
    path("search/", views.Search.as_view(), name='search'),
    path("json-filter/", views.JsonFilterMoviesView.as_view(), name='json_filter'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("<slug:slug>/", views.WeaponDetailView.as_view(), name="weapon_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("country/<str:slug>/", views.CountryView.as_view(), name="country_detail")
]