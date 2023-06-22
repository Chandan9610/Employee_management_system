from django.urls import path
from officeauth import views

urlpatterns = [
    path('',views.handlelogin,name="handlelogin"),
    path('logout/',views.handlelogout,name="handlelogout"),
]