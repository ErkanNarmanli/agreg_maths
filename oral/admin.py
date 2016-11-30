from django.contrib import admin
from rules.contrib.admin import ObjectPermissionsModelAdmin
from .models import Lesson, LessonTemplate, Reference, Development,\
                EffectiveDevelopment


class LessonTemplateAdmin(admin.ModelAdmin):
    list_display = ['title', 'num']
    ordering = ['num']


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'author']
    ordering = ['title']


class LessonAdmin(ObjectPermissionsModelAdmin):
    pass

admin.site.register(LessonTemplate, LessonTemplateAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Development)
admin.site.register(EffectiveDevelopment)
