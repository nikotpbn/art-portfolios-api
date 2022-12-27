from .api.views import CustomAuthToken, UserAuthenticated
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('me/', UserAuthenticated.as_view(), name='me'),
]





