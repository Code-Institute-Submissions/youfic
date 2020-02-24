from django.urls import path, include
from accounts.views import index, logout, login, registration, user_profile

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('register/', registration, name="registration"),
    path('profile/', user_profile, name="profile"),
]
