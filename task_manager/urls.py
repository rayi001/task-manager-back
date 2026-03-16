"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from authentication import views as auth_views

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    return Response({
        'message': 'Task Manager API',
        'version': '1.0.0',
        'endpoints': {
            'register': '/api/register/',
            'login': '/api/login/',
            'profile': '/api/profile/',
            'token_refresh': '/api/token/refresh/',
            'tasks': '/api/'
        }
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return Response({
        'status': 'healthy',
        'message': 'Task Manager API is running',
        'version': '1.0.0'
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def root_view(request):
    return Response({
        'message': 'Task Manager API',
        'version': '1.0.0',
        'endpoints': {
            'register': '/api/register/',
            'login': '/api/login/',
            'profile': '/api/profile/',
            'token_refresh': '/api/token/refresh/',
            'tasks': '/api/'
        }
    })

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('api/', api_root, name='api_root'),
    path('', root_view, name='root_view'),  # Dedicated root view
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('api/register/', auth_views.register, name='register'),
    path('api/login/', auth_views.login, name='login'),
    path('api/profile/', auth_views.profile, name='profile'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Task URLs
    path('api/', include('tasks.urls')),
]
