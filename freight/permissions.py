from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Load

class IsFreightCompany(BasePermission):
    '''
        checks if user of the request has a freight company relation which
        makes it a freight company
    '''
    def has_permission(self, request, view):
        try:
            freight_company = request.user.freightcompany
            return True
        except Exception as e:
            return False

    def has_object_permission(self, request, view, obj):
        print(isinstance(obj, Load))
        if isinstance(obj, Load):
            return False
        return True

class IsFactory(BasePermission):
    '''
        checks if user of the request has a freight company relation which
        makes it a freight company
    '''
    def has_permission(self, request, view):
        try:
            factory = request.user.factory
            return True
        except Exception as e:
            return False
    
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)