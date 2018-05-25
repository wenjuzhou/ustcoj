from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    url(r'^groups/$', views.UserGroupList.as_view()),
    url(r'^login$', views.LogIn),
    url(r'^logout$',views.LogOut),
    url(r'^register$',views.UserRegister.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)