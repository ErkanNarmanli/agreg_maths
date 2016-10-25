from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Lesson, LessonTemplate


# class LessonList(ListView):
#     template_name = "agreg/lesson_list.html"
#     context_object_name = 'lesson_list'
# 
#     def get_queryset(self):
#         return Lesson.objects.order_by('num')
 
 
class LessonDetail(DetailView):
    template_name = "oral/lesson_detail.html"
    
    def get_object(self):
        self.page_user = get_object_or_404(User, username=self.args[0])
        self.template = get_object_or_404(LessonTemplate, num=self.args[1])
        return get_object_or_404(Lesson, author=self.page_user, template=self.template)


# class ReferenceList(ListView):
#     model = Reference
#     template_name = "agreg/ref_list.html"
#     context_object_name = 'ref_list'
# 
# 
# class ReferenceDetail(DetailView):
#     model = Reference
#     template_name = "agreg/ref_detail.html"
