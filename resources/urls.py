from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from resources import views

urlpatterns = [
    url(r'^armor/$', views.ArmorList.as_view()),
    url(r'^armor/(?P<pk>[0-9]+)/$', views.ArmorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)