from django.urls import path

from .views import (
    Tuition_languageList,
    Tuition_languageDetail,
    Education_formList,
    Education_formDetail,
    SubjectList,
    SubjectDetail,
    FacultyList,
    FacultyDetail,
    UniversityList,
    UniversityDetail
)
urlpatterns=[
    path('tuition-language/', Tuition_languageList.as_view(), name='tuition_language'),
    path('tuition-language/<int:pk>/', Tuition_languageDetail.as_view()),

    path('education-form/', Education_formList.as_view(), name='education_form'),
    path('education-form/<int:pk>/', Education_formDetail.as_view()),

    path('subject/', SubjectList.as_view(), name='subject'),
    path('subject/<int:pk>/', SubjectDetail.as_view()),

    path('faculty/', FacultyList.as_view(), name='faculty'),
    path('faculty/<int:pk>/', FacultyDetail.as_view()),

    path('university/', UniversityList.as_view(), name='university'),
    path('university/<int:pk>/', UniversityDetail.as_view()),
]
