from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer, RegisterSerializer
from .models import Student

class StudentView(generics.CreateAPIView):
    serializer_class = StudentSerializer
    
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
