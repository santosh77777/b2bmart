from django.urls import path
from . import views
app_name="product"

urlpatterns = [
    path("",views.HomeView, name="home"),
    path("category/",views.category, name="category"),
    path("<str:slug>/",views.HomeProductList.as_view(), name="home_list")
]
