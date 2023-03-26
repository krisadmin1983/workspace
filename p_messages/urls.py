from django.urls import path
from .views import post_message, community_messages
from . import views

app_name = 'p_messages'

urlpatterns = [
    path('post-message/', post_message, name='post_message'),
    path('community-messages/', views.community_messages, name='community_messages'),
]
