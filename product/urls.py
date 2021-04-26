from django.urls import path
from . import views
app_name = "product"


urlpatterns = [
    path('', views.index, name="index"),
    path('category/',views.category, name="category"),
]