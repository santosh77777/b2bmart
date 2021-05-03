from django.urls import path
from . import views
app_name="product"

urlpatterns = [
    path("",views.HomeView, name="home_list"),
    path("category/",views.category, name="category"),
    # path(r'^homescroll/$',views.homescroll, name="homescroll"),
    path("<str:slug>/",views.WebsiteHomeList.as_view(), name="website_home_list")
]
