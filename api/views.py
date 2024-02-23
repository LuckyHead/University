from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *

from .serializers import (
    Tuition_languageSerializer,
    Education_formSerializer,
    SubjectSerializer,
    FacultySerializer,
    UniversitySerializer,
)

from faculty_fields.models import (
    Tuition_language,
    Education_form,
    Subject,
)

from faculty.models import Faculty
from university.models import University

class Tuition_languageList(APIView):

    def get(self, request, format=None):
        queryset= Tuition_language.objects.all()
        serializer=Tuition_languageSerializer(queryset, many=True, context={'request': request})
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request, format=None):
        serializer=Tuition_languageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(),
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )
    
class Tuition_languageDetail(APIView):

    def get_object(self,pk):
        try:
            return Tuition_language.objects.get(pk=pk)
        except Tuition_language.DoesNotExist:
            return Response(
                'Not found'
            )
    
    def get(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=Tuition_languageSerializer(queryset)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def put(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=Tuition_languageSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_406_NOT_ACCEPTABLE
        )
    
    def patch(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=Tuition_languageSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_406_NOT_ACCEPTABLE
        )
    
    def delete(self, request, pk, format=None):
        queryset=self.get_object(pk)
        queryset.delete()
        return Response(
            'Deleted',
            status=HTTP_204_NO_CONTENT
        )


class Education_formList(APIView):

    def get(self, request, format=None):
        queryset= Education_form.objects.all()
        serializer=Education_formSerializer(queryset, many=True, context={'request': request})
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request, format=None):
        serializer=Education_formSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(),
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )
    
class Education_formDetail(APIView):

    def get_object(self,pk):
        try:
            return Education_form.objects.get(pk=pk)
        except Education_form.DoesNotExist:
            return Response(
                'Not found'
            )
    
    def get(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=Tuition_languageSerializer(queryset)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def put(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=Education_formSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_406_NOT_ACCEPTABLE
        )
    
    def patch(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=Education_formSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_406_NOT_ACCEPTABLE
        )
    
    def delete(self, request, pk, format=None):
        queryset=self.get_object(pk)
        queryset.delete()
        return Response(
            'Deleted',
            status=HTTP_204_NO_CONTENT
        )
    
class SubjectList(APIView):

    def get(self, request, format=None):
        queryset= Subject.objects.all()
        serializer=SubjectSerializer(queryset, many=True, context={'request': request})
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request, format=None):
        serializer=SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(),
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )

class SubjectDetail(APIView):

    def get_object(self,pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response(
                'Not found'
            )
    
    def get(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=SubjectSerializer(queryset)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def put(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=SubjectSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_406_NOT_ACCEPTABLE
        )
    
    def patch(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=SubjectSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_406_NOT_ACCEPTABLE
        )
    
    def delete(self, request, pk, format=None):
        queryset=self.get_object(pk)
        queryset.delete()
        return Response(
            'Deleted',
            status=HTTP_204_NO_CONTENT
        )
    
class FacultyList(APIView):

    def get(self, request, format=None):
        queryset= Faculty.objects.all()
        serializer=FacultySerializer(queryset, many=True, context={'request': request})
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request, format=None):
        serializer=FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(),
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )
    
class FacultyDetail(APIView):

    def get_object(self,pk):
        try:
            return Faculty.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            return Response(
                'Not found'
            )
    
    def get(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=FacultySerializer(queryset)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def put(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=FacultySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_406_NOT_ACCEPTABLE
        )
    
    def patch(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=FacultySerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_406_NOT_ACCEPTABLE
        )
    
    def delete(self, request, pk, format=None):
        queryset=self.get_object(pk)
        queryset.delete()
        return Response(
            'Deleted',
            status=HTTP_204_NO_CONTENT
        )
    
class UniversityList(APIView):

    def get(self, request, format=None):
        queryset= University.objects.all()
        serializer=UniversitySerializer(queryset, many=True, context={'request': request})
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request, format=None):
        serializer=UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(),
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )

class UniversityDetail(APIView):

    def get_object(self,pk):
        try:
            return University.objects.get(pk=pk)
        except University.DoesNotExist:
            return Response(
                'Not found'
            )
    
    def get(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=UniversitySerializer(queryset)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def put(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=UniversitySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_406_NOT_ACCEPTABLE
        )
    
    def patch(self, request, pk, format=None):
        queryset=self.get_object(pk)
        serializer=UniversitySerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializer.errors,
            status=HTTP_406_NOT_ACCEPTABLE
        )
    
    def delete(self, request, pk, format=None):
        queryset=self.get_object(pk)
        queryset.delete()
        return Response(
            'Deleted',
            status=HTTP_204_NO_CONTENT
        )