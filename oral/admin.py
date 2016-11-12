from django.contrib import admin
from .models import Lesson, LessonTemplate, Reference, Development,\
                    LessonDevelopment


class LessonTemplateAdmin(admin.ModelAdmin):
    list_display = ['title', 'num']
    ordering = ['num']


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'author']
    ordering = ['title']


class LessonDevelopmentInline(admin.TabularInline):
    model = LessonDevelopment
    extra = 0


class LessonAdmin(admin.ModelAdmin):
    inlines = [LessonDevelopmentInline]

admin.site.register(LessonTemplate, LessonTemplateAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Development)
