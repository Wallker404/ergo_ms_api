"""
Базовые классы представлений API.
"""

from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework import permissions

class BaseAPIView(APIView):
    """
    Базовый класс для всех API представлений.
    
    Включает:
    - JWT аутентификацию
    - Аутентификацию через сессии
    """
    authentication_classes = [JWTAuthentication] 
    throttle_classes = [AnonRateThrottle, UserRateThrottle]