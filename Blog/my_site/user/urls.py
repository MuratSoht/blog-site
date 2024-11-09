from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import LoginUser
app_name = 'user'
urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
