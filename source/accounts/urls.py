﻿from accounts.views import LoginView, RegisterView , logout_view
from django.urls import path


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout')
]