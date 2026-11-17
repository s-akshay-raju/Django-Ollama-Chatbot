from django.urls import path
from . import views

urlpatterns = [
    path("",views.experiment,name="experiment"),
    path("chatbot/",views.chatbot,name="chatbot")
]