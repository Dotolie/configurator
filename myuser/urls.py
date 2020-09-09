from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('', views.index, name='index' ),
    path('login/', views.login, name='login'  ),
    path('logout/', views.logout, name='logout'  ),
    path('save/', views.save, name='save' ),
    path('restart/', views.restart, name='restart' ),
    path('shutdown/', views.shutdown, name='shutdown' ),

]