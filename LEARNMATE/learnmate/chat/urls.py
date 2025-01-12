from django.urls import path
from .views import chat_api
from .views import home


urlpatterns = [
    path('chat/', chat_api, name='chat_api'),
    path('', home, name='home'),

]



