from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=225)
    email=models.EmailField(unique=True)  # The 'unique=True' ensures no two users have the same email.
    
    def __str__(self):
         # This method returns a string representation of the object.
        return self.name
    
class UploadedImage(models.Model):
    image = CloudinaryField('image')  # Cloudinary field to store image
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"