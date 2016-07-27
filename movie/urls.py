from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^action$', views.action, name='action'),
    url(r'^annimation$', views.annimation, name='annimation'),
    url(r'^fantasy$', views.fantasy, name='fantasy'),
    url(r'^sci_fi$', views.sci_fi, name='sci_fi'),

]
