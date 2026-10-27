# write code to call method in views.py from urls.py
# adding a comment here to test the Github Actions workflow
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('ab/', views.about, name='about'),
]