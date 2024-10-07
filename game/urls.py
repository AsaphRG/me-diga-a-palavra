from django.urls import path
from game import views

app_name = 'forca'

urlpatterns = [
    path('', views.home, name='home'),

    path('user/login/', views.login, name='login'),
    path('user/register/', views.register, name='register'),
    path('user/update/', views.modify, name='modify'),
    path('user/logout/', views.logout, name='logout'),
    path('user/games', views.games, name='games'),

    path('theme/', views.theme, name='theme'),
    path('new_game/', views.createGame, name='new_game'),
    path('game/<int:id>/', views.game, name='game'),
    path('game_over/', views.game_over, name='game_over')

    # path('load_all', views.load_all, name='load_all'),
]
