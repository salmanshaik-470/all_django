from . import views
from django.urls import path,include
urlpatterns = [
    path('',views.index,name='base'),
    path('home',views.home,name='home'),
    path('std',views.student_details,name='std')
]