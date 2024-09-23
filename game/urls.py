from django.urls import path
from game import views

app_name = 'forca'

urlpatterns = [
    path('', views.home, name='home'),

    path('user/login/', views.login, name='login'),
    path('user/register/', views.register, name='register'),
    path('user/update/', views.modify, name='modify'),
    path('user/logout/', views.logout, name='logout')
]
