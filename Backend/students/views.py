from rest_framework import generics
from .models import Student
from .serializers import StudentSerializers

# Create your views here.

class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers