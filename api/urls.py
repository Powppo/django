from django.urls import path
from .views import StudentView, RegisterView

urlpatterns = [
    path('student/', StudentView.as_view(), name='student_list'),
    path('register/', RegisterView.as_view(), name='user_register'),
]
