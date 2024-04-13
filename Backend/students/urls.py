from django.urls import path
from .views import StudentCreate, StudentList

urlpatterns = [
    path('register_student_records/', StudentCreate.as_view(), name="student-create"),
    path('List_student_records/', StudentList.as_view(), name="student-list"),
]

# keep endpoint names of path distinct from other projects
# check if any other projects has same endpoint name as this one