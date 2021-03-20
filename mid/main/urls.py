from django.urls import path, re_path
from .views import index, login_page, register_page, logout_user


urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_user, name='logout')
]
