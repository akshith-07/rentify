
from django.urls import path, include
from . import views
    
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),    
    path('users/', views.UserListView.as_view()),
    path('users/profile/', views.UserProfileListView.as_view()),
    path('users/create/', views.UserCreateView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),

]
