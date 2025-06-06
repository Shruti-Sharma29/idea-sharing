# admin username ---> ijk
# admin password ---> ijk

from django.urls import path
from ideas import views

urlpatterns = [
    path('', views.mainpage, name="main"),
    path('home', views.homepage, name="home"),
    path('share', views.sharepage, name="content"),
    path('saving', views.saveinfo, name="save"),
    path("delete-data/<int:xyz>", views.deleteinfo, name = "deleting"),
    path('login', views.loginpage, name="login"),
    path('register', views.registerpage, name="signup"),
    path('logout', views.logoutpage, name="logout"),
]