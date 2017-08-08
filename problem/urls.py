from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.problem_list, name='problem_list'),
    url(r'^(?P<problem_id>[0-9]+)/$', views.problem_detail, name='problem_detail'),
]