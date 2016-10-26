from django.contrib import admin
from .models import Lesson, LessonTemplate, Reference, Development


class LessonTemplateAdmin(admin.ModelAdmin):
    list_display = ['title', 'num']
    ordering = ['num']

class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'author']
    ordering = ['title']

admin.site.register(LessonTemplate, LessonTemplateAdmin)
admin.site.register(Lesson)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Development)
