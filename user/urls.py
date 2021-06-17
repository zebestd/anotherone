from django.urls import include, path
from . import views


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register/', views.registerPage, name="register"),
    #path('profil/', views.userPage, name="user-page"),
    path('profile/', views.profile, name='user-profile'),
    path('', views.ustalist, name="usta"),
	path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),    
    path('ajax/load-ilce/', views.load_ilce, name='ajax_load_ilce'),
    path('addusta/', views.createUsta, name="create_usta")

    
   ] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)