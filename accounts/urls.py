from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),  
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
      path('admin/', admin.site.urls),
]