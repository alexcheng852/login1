from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r"^", include("users.urls")),
    url(r"^admin/", admin.site.urls),
    url(r"^", include("website.urls")),
]