from django.urls import path
from . import views
app_name="product"

urlpatterns = [
    path("",views.HomeView.as_view(), name="home"),
    path("category/",views.category, name="category"),
    path("list/<str:username>/",views.HomeProductList.as_view(), name="home_list")
]
