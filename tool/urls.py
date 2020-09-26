from django.urls import path
from tool import views

urlpatterns = [
    path('', views.tool_detail, name="tool_detail"),
    path('', views.tool_results, name='tool_results'),
]
