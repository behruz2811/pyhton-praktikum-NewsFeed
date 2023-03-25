from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import UserLoginView, DashboardView

urlpatterns = [
    # path('login/', UserLoginView, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', DashboardView, name='user-profile')
]