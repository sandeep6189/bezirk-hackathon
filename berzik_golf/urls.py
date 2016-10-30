from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^move/?$',views.move,name='move'),
    url(r'^update_beacon/?$',views.update_beacon,name='update_beacon'),
    url(r'^update_direction/?$',views.update_direction,name='update_direction'),
]