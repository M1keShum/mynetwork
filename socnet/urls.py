from django.urls import path
from .views import userpage, addmessage


urlpatterns = [
    path('', userpage, name="userpage"),
    path('addmessage/', addmessage, name='addmessage')
]
