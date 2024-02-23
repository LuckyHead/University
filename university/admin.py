from django.contrib.admin import *
from university.models import *

@register(University)
class UniversityAdmin(ModelAdmin):
    list_display=('id','name')
    list_display_links=('id','name')
    ordering=('name',)