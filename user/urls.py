from django.urls import include, path
from . import views




urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('user/', views.userPage, name="user-page"),
    path('', views.home, name="home"),
    path('list/', views.ustalist, name="usta"),
	path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),    
    path('ajax/load-ilce/', views.load_ilce, name='ajax_load_ilce'),
    path('addusta/', views.createUsta, name="create_usta")

    
   ]