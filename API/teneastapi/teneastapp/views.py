# API/teneastapi/teneastapp/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Inquiry
from .serializers import InquirySerializer, UserSerializer, RegisterSerializer

class InquiryCreateView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        questions = request.data.get('questions')
        answers = request.data.get('answers')
        
        if not user.is_authenticated:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        inquiry = Inquiry.objects.create(user=user, questions=questions, answers=answers)
        return Response({'message': 'Inquiry submitted successfully'}, status=status.HTTP_201_CREATED)

class InquiryListView(generics.ListAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

class InquiryDetailView(generics.RetrieveAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer