from django.urls import path

from . import views

urlpatterns = [
    path('signup.html', views.signup_view, name='signup'),
    path('login.html', views.login_view, name='login'),
]
