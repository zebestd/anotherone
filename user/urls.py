from django.urls import include, path
from . import views




urlpatterns = [
    path('', views.UstaListView.as_view(), name='usta_changelist'),
    path('add/', views.UstaCreateView.as_view(), name='usta_add'),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),    
    path('<int:pk>/', views.UstaUpdateView.as_view(), name='usta_change'),
    path('ajax/load-ilce/', views.load_ilce, name='ajax_load_ilce'),

    
   ]