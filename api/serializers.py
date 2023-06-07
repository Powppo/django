from rest_framework import serializers
from .models import StudentRegister
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('studentId',
                  'FirstName',
                  'LastName',
                  'RegistrationNo',
                  'Email',
                  'Course')
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRegister
        fields = ('username',
                  'email',
                  'password')