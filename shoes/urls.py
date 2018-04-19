from django.conf.urls import url
from shoes import views
from rest_framework.decorators import api_view


urlpatterns = [
    url(r'^shoes/$', views.shoes_list),
]
