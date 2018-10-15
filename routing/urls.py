from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^simple_route/$", views.simple_route),
    url(r"^simple_route/([\w]+)$", views.simple_route),
    url(r"^slug_route/([0-9\w\-\_]{1,16})/$", views.slug_route),
    url(r"^sum_route/([\-\d]+)/([\-\d]+)/$", views.sum_route),
    url(r"^sum_get_method/$", views.sum_get_method),
    url(r"^sum_post_method/$", views.sum_post_method, name="test"),
]
