from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('about/', views.about, name='about'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
    path('profile/', views.profile, name='profile'),
]
