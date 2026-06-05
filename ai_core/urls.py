from django.urls import path
from . import views

app_name = 'ai_core'
urlpatterns = [path('mcp-task/', views.mcp_task, name='mcp_task')]
