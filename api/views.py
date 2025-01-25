from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from .models import UploadedImage
from .serializers import UploadedImageSerializer
class UserList(APIView):
     # Require authentication for all methods
    permission_classes = [IsAuthenticated]

    # GET method: Retrieve all users
    def get(self, request):
        # Query the database for all user records.
        users = User.objects.all()
        
        # Serialize the queryset into a JSON-compatible format.
        serializer = UserSerializer(users, many=True)  # many=True because we expect multiple users.
        
        # Return the serialized data with a 200 OK HTTP status.
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST method: Add a new user
    def post(self, request):
        # Deserialize the incoming JSON data to validate and create a new User instance.
        serializer = UserSerializer(data=request.data)
        
        # If data is valid, save it to the database.
        if serializer.is_valid():
            serializer.save()
            # Return the created user with a 201 Created HTTP status.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If validation fails, return errors with a 400 Bad Request HTTP status.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    # Require authentication for delete operations
    permission_classes = [IsAuthenticated]

    # DELETE method: Delete a user by ID
    def delete(self, request, id):
        try:
            # Try to find the user with the given ID.
            user = User.objects.get(id=id)
            
            # If found, delete the user from the database.
            user.delete()
            
            # Return a success message with a 200 OK HTTP status.
            return Response(
                {"message": f"User with ID {id} deleted successfully"},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            # If no user is found with the given ID, return a 404 Not Found error.
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
class ImageUploadView(APIView):
    def post(self, request):
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)