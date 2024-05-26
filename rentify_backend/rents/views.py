from django.core.mail import send_mail
from django.http import JsonResponse
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Property
from .serializer import PropertyCreateUpdateSerializer, PropertyListSerializer , PropertyDetailSerializer

class PropertyInterestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        property_id = request.data.get('property_id')
        property = Property.objects.get(id=property_id)
        seller_email = property.seller.email
        buyer_name = request.user.get_full_name()
        buyer_email = request.user.email 
        property_title = property.place
        email_subject = _('Interest in your property')
        email_body = f"Hi,\n\n{buyer_name} is interested in your property '{property_title}'.\n\nYou can contact them at {buyer_email}.\n\nRegards,\nYour Website Name"
        send_mail(
            email_subject,
            email_body,
            buyer_email,  
            [seller_email],
            fail_silently=False,
        )
        return JsonResponse({'message': "Email sent successfully"}, status=status.HTTP_200_OK)
    
class PropertyCreateListView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PropertyCreateUpdateSerializer
        return PropertyListSerializer

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(seller=self.request.user)

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(seller=self.request.user)


class PropertyPublicListView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view public properties