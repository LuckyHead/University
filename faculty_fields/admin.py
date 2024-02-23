from django.contrib.admin import *

from .models import(
    Tuition_language,
    Education_form,
    Subject
)

@register(Tuition_language)
class TuitionlanguageAdmin(ModelAdmin):
    list_display=('id', 'language')
    list_display_links=('id', 'language')

@register(Education_form)
class EducationformAdmin(ModelAdmin):
    list_display=('id', 'name')
    list_display_links=('id', 'name')

@register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display=('id', 'name')
    list_display_links=('id', 'name')
