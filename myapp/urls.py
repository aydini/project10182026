# write code to call method in views.py from urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('ab/', views.about, name='about'),
]