from django.conf.urls import url
from basic_app import views

# Template Tagging
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
    url(r'^base/$', views.base, name='base'),
    url(r'^$', views.index, name='index'),

]
