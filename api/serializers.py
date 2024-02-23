from rest_framework.serializers import ModelSerializer

from faculty_fields.models import(
    Tuition_language,
    Education_form,
    Subject
)

from faculty.models import Faculty
from university.models import University

class Tuition_languageSerializer(ModelSerializer):
    class Meta:
        model=Tuition_language
        fields='__all__'

class Education_formSerializer(ModelSerializer):
    class Meta:
        model=Education_form
        fields='__all__'   

class SubjectSerializer(ModelSerializer):
    class Meta:
        model=Subject
        fields='__all__'

class FacultySerializer(ModelSerializer):
    class Meta:
        model=Faculty
        fields='__all__'

class UniversitySerializer(ModelSerializer):
    class Meta:
        model=University
        fields='__all__'