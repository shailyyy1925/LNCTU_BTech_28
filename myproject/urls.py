from django.contrib import admin
from django.urls import path
from LNCTU_BTech_28.myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
