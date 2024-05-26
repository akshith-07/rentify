from django.shortcuts import render
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework import generics, status , views
from rest_framework.permissions import AllowAny
from django.http import Http404, HttpResponse, JsonResponse, StreamingHttpResponse
from rest_framework.response import Response
from django.db import connection
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Permission
from django.shortcuts import get_object_or_404
from .serializer import UserListSerializer
from django.apps import apps
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import User
from rest_framework.permissions import AllowAny


# Create your views here.

class UserProfileListView(generics.ListAPIView):
    serializer_class= UserListSerializer
 
    def get_queryset(self):
        user=self.request.user
        queryset = User.objects.filter(id=user.id)
        return queryset
 

class UserCreateView(views.APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save() 
        return Response({'pk': user.pk}, status=status.HTTP_201_CREATED)


class UserDetailView(views.APIView):
 
    serializer_class = UserListSerializer
    queryset = User.objects.all()
 
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
 
    def get(self, request, pk, **kwargs):
        user = self.get_object(pk)
        serializer = UserListSerializer(instance=user)
        data = serializer.data
        return Response(data)
   
    def patch(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = get_object_or_404(User, pk=user_pk)
        serializer = UserListSerializer(instance=user, data=request.data, partial=True)  # Use partial=True to allow partial updates
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'pk': user.pk}, status=status.HTTP_200_OK)
    
 
class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
 
    def get_queryset(self):
        # Fetch the user instance
        user=self.request.user
        if user.is_staff:
            queryset = User.objects.all()
        else:
            queryset = User.objects.filter(id=user.id)
 
        return queryset