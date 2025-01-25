from rest_framework import serializers
from .models import User
from .models import UploadedImage
class UserSerializer(serializers.ModelSerializer):
    # Meta class specifies the model and fields to include in the serialized output.
    class Meta:
        model = User  # Tells the serializer to use the User model.
        fields = ['id', 'name', 'email']  # Specifies which fields to include in API responses.
class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ['id', 'image', 'uploaded_at']