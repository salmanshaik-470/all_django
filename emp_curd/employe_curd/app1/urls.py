from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.add_event),
    path('delete/<int:id>',views.delete_data,name='delete'),
    path('update/<int:id>',views.update,name="update"),
    path('signup/', views.signuppage, name="signuppage"),
    path('login/', views.loginpage, name="loginpage"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logoutuser, name="logout"),

]