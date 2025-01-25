from django.contrib import admin
from .models import User, UploadedImage

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')  # Columns to display in the list view
    search_fields = ('name', 'email')      # Fields to search by
    ordering = ('id',)                     # Default ordering


@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at', 'image_preview')  # Display columns
    readonly_fields = ('image_preview',)                           # Make preview read-only

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px;" />'
        return "No image"
    image_preview.allow_tags = True
    image_preview.short_description = "Preview"
