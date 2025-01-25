from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    # URL for retrieving and creating users.
    path('users', UserList.as_view(), name='user-list'),
    
    # URL for deleting a specific user by ID.
    path('users/<int:id>', UserDetail.as_view(), name='user-detail'),
]
