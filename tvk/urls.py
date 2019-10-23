
from django.urls import path, include

from tvk import views

urlpatterns = [
    path('', views.LogMainView, name='main_log'),
]
