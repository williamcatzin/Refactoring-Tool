"""refactoring_tool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tool import views as tool_views
from analytics import views as analytics_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tool_views.tool_detail, name='tool_detail'),
    path('tool/results/', tool_views.tool_results, name='tool_results'),
    path('analytics/', analytics_views.analytics_detail, name='analytics_detail')
]
