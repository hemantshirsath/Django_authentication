from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login_user,name="login"),
    path('profile/',views.profile,name="profile"),
    path('logout/',views.user_logout,name="logout"),
    path('passchange/',views.passchange,name="passchange"),
    path('passchange1/',views.passchange1,name="passchange1"),
    path('userdetail/<int:id>',views.userdetail,name="userdetail")
]
