# mysite/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("ButtonAlert/", include("ButtonAlert.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]