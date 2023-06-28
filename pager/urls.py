from django.urls import path

from . import views

app_name = 'polls'
app_name = 'pager'

urlpatterns = [
    path('', views.index, name = 'index'),
]