from django.contrib import admin
from django.urls import include, path
from authentication import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup,name='signu'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('work/',views.work,name='work'),
    

]
34