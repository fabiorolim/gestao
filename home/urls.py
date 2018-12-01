from django.urls import path, include
from .views import home, my_logout

urlpatterns = [
    path('', home, name='home_url'),
    path('logout/', my_logout, name='logout_url')
]
