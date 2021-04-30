from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('help/', TemplateView.as_view(template_name="help.html"), name="help"),

    path('about-us/', TemplateView.as_view(template_name="company/about-us.html"), name="about_us"),
    path('about-management/', TemplateView.as_view(template_name="company/management.html"), name="about_management"),
    path('about-media-center/', TemplateView.as_view(template_name="company/media-center.html"), name="about_media_center"),
    path('about-work-with-us/', TemplateView.as_view(template_name="company/workWithUs.html"), name="about_work_with_us"),
    path('about-contact-us/', TemplateView.as_view(template_name="company/contact-us.html"), name="about_contact_us"),
    path('help-center/', TemplateView.as_view(template_name="company/help.html"), name="help_center"),
    path('privacy-policy/', TemplateView.as_view(template_name="company/privacy-policy.html"), name="privacy_policy"),
    path('trading-policy/', TemplateView.as_view(template_name="company/trading-policy.html"), name="trading_policy"),
    path('term-condition/', TemplateView.as_view(template_name="company/term-condition.html"), name="term_condition"),
    path('edit-profile/', TemplateView.as_view(template_name="company/seller/user.html.html"), name="edit_profile"),
    path('certificate/', TemplateView.as_view(template_name="company/certificate.html"), name="certificate"),
    path('media-center/', TemplateView.as_view(template_name="company/media-center.html"), name="media_center"),
    path('advertise/', TemplateView.as_view(template_name="company/advertise.html"), name="advertise"),

    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('accounts/', include('allauth.urls')),
    path('', include("product.urls", namespace="product")),
    path('dashboard/', include('dashboard.urls', namespace="dashboard")),

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
