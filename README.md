User Management API with Django and Cloudinary Storage
Overview
This is a User Management API built using Django and Django REST Framework. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on user profiles, including managing user data and profile images. The profile images are stored using Cloudinary, a cloud-based storage service optimized for media management.

Features
User Registration: Create new user accounts with basic details.

User Authentication: Secure authentication using tokens or session-based authentication.

Profile Management: Update and retrieve user profiles, including profile images.

Cloudinary Integration: Store and manage user profile images efficiently using Cloudinary.

API Endpoints: RESTful endpoints for managing users and their profiles.

Prerequisites
Before running the project, ensure you have the following installed:

Python 3.8 or higher

Django 4.x or higher

Django REST Framework

Cloudinary Python SDK

A Cloudinary account (for media storage)

Installation
Clone the Repository:

git clone https://github.com/m1k2it9ad/user_manager_api.git
cd user-management-api


Set Up a Virtual Environment:


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
pip install -r requirements.txt
Set Up Cloudinary:

Sign up for a Cloudinary account if you don't have one.

Obtain your CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, and CLOUDINARY_API_SECRET from the Cloudinary dashboard.

Add these credentials to your .env file:


CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret


Run Migrations:

python manage.py migrate
Create a Superuser:


python manage.py createsuperuser


Run the Development Server:


python manage.py runserver
API Endpoints
Authentication
Register a User: POST /api/register/

Login: POST /api/login/

Logout: POST /api/logout/

User Management
Get All Users: GET /api/users/

Get User Details: GET /api/users/<id>/

Update User Profile: PUT /api/users/<id>/

Delete User: DELETE /api/users/<id>/



Profile Image Management
Upload Profile Image: POST /api/users/<id>/upload-image/

Update Profile Image: PUT /api/users/<id>/update-image/

Delete Profile Image: DELETE /api/users/<id>/delete-image/


Environment Variables
Create a .env file in the root directory and add the following variables:


SECRET_KEY=your_django_secret_key
DEBUG=True
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
Cloudinary Configuration
To integrate Cloudinary with Django, add the following to your settings.py:

import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)
Example Requests
Register a User
bash
Copy
curl -X POST http://127.0.0.1:8000/api/register/ \
-H "Content-Type: application/json" \
-d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "securepassword123"
}'


Upload Profile Image:

curl -X POST http://127.0.0.1:8000/api/users/1/upload-image/ \
-H "Authorization: Token your_token_here" \
-F "image=@path_to_your_image.jpg"


Testing
To run tests, use the following command:

python manage.py test


Contributing:
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Submit a pull request with a detailed description of your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Django for the web framework.

Django REST Framework for building the API.

Cloudinary for media storage and management.

Contact
For any questions or issues, please open an issue on GitHub or contact the maintainer at michaelt5593@gmail.com
