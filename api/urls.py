from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserList, UserDetail

urlpatterns = [
     # JWT Token endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #protected CRUD endpoints:
    path('users', UserList.as_view(), name='user-list'),# URL for retrieving and creating users.
    path('users/<int:id>', UserDetail.as_view(), name='user-detail'),# URL for deleting a specific user by ID.
    
]
