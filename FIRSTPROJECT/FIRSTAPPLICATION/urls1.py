from django.conf.urls import url
from FIRSTAPPLICATION import views

urlpatterns=[
    url(r'^$', views.content, name='content'),
]
