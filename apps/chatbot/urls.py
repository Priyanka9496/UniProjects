from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.chatbot_ui, name='chatbot_ui'),
    path('api/', views.chatbot_api, name='chatbot_api'),
]
