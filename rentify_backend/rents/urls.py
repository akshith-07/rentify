from django.urls import path
from .views import PropertyCreateListView, PropertyDetailView, PropertyPublicListView , PropertyInterestView

urlpatterns = [
    path('my-properties/', PropertyCreateListView.as_view(), name='property-create-list'),
    path('my-properties/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
    path('public-properties/', PropertyPublicListView.as_view(), name='public-property-list'),
    path('property/interest/', PropertyInterestView.as_view(), name='property-interest'),

]
