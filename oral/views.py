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

class LessonList(TemplateView):
    template_name = "oral/lesson_list.html"

    def get_context_data(self, **kwargs):
        context = super(LessonList, self).get_context_data(**kwargs)
        page_user = get_object_or_404(User, username=self.args[0])
        is_info = (page_user.profil.option == 'D')
        user_year = page_user.profil.year
        algebre_lessons = LessonTemplate.objects.filter(year=user_year,
                                                       category='algebre',)
        analyse_lessons = LessonTemplate.objects.filter(year=user_year,
                                                       category='analyse')
        if is_info:
            algebre_lessons = algebre_lessons.filter(is_for_info=True).order_by('num')
            analyse_lessons = analyse_lessons.filter(is_for_info=True).order_by('num')
            info_lessons = LessonTemplate.objects.filter(year=user_year,
                                                        category='informatique',)
            info_lessons = info_lessons.order_by('num')
        context['page_user'] = page_user
        context['is_info'] = is_info
        context['algebre_lessons'] = algebre_lessons
        context['analyse_lessons'] = analyse_lessons
        if is_info:
            context['info_lessons'] = info_lessons
        return context

 
 
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
