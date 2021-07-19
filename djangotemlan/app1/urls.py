from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('index',views.index,name='index'),
    path('cont',views.contact,name='contact'),
    path('cond',views.condition,name='cond')
]