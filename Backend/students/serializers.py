from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_rollno', 'student_name', 'student_email', 'student_city', 'student_percentage']