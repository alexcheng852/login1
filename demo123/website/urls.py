from django.conf.urls import url
from website.views import index, services

urlpatterns = [
    url(r"^index/", index, name="index"),
    url(r"^services/",services, name="services"),
]
