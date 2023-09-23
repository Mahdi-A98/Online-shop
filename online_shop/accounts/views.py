from rest_framework.views import Response, APIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import update_last_login
from rest_framework.views import Response
import jwt, datetime
from .models import User
from .serializer import UserSerializer

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

