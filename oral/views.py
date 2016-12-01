from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, TemplateView, UpdateView, ListView
from rules.contrib.views import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from .models import Lesson, LessonTemplate, Development

@method_decorator(login_required, name='dispatch')
class LessonCreate(View):
    def get(self, request, username, template_num):
        page_user = get_object_or_404(User, username=username)
        if request.user.username == page_user.username:
            template = get_object_or_404(
                    LessonTemplate,
                    num=template_num,
                    year=page_user.profil.year
                    )
            if page_user.lessons.filter(template=template):
                messages.error(request, "Nope, la leçon existe déjà")
                return HttpResponseRedirect(reverse_lazy(
                                                "oral:lessons",
                                                args=[request.user.username]
                                                ))
            else:
                Lesson.objects.create(
                        template=template,
                        author=request.user,
                        is_finished=False,
                    )
                messages.success(request, "La leçon a été créé !")
                return HttpResponseRedirect(reverse_lazy(
                                            "oral:detail",
                                            args=[request.user.username,
                                                  str(template_num)],
                                            ))
        else:
            messages.error(request, "Nope, c'est pas à toi, ça !")
            return HttpResponseRedirect(reverse_lazy(
                                            "oral:lessons",
                                            args=[request.user.username]
                                            ))


@method_decorator(login_required, name='dispatch')
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
            algebre_lessons = algebre_lessons.filter(is_for_info=True) \
                                             .order_by('num')
            analyse_lessons = analyse_lessons.filter(is_for_info=True) \
                                             .order_by('num')
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


@method_decorator(login_required, name='dispatch')
class DevList(ListView):
    model = Development
    template_name = "oral/dev_list.html"
    context_object_name = 'dev_list'
 

@method_decorator(login_required, name='dispatch')
class DevDetail(DetailView):
    template_name = "oral/dev_detail.html"
    model = Development


@method_decorator(login_required, name='dispatch')
class LessonDetail(DetailView):
    template_name = "oral/lesson_detail.html"
    
    def get_object(self):
        self.page_user = get_object_or_404(User, username=self.args[0])
        self.template = get_object_or_404(LessonTemplate, num=self.args[1], year=self.page_user.profil.year)
        return get_object_or_404(Lesson, author=self.page_user, template=self.template)

    def get_context_data(self, **kwargs):
        context = super(LessonDetail, self).get_context_data(**kwargs)
        page_user = get_object_or_404(User, username=self.args[0])
        template = get_object_or_404(LessonTemplate, num=self.args[1], year=self.page_user.profil.year)
        context['developments'] = template.allDevs.filter(
                                                        user=page_user,
                                                        )
        return context

class AjaxLessonUpdateContent(PermissionRequiredMixin, UpdateView):
    # permission
    permission_required = 'oral.change_lesson'
    # arg 0 : username
    # arg 1 : lesson number
    template_name = "oral/ajax/lesson_update_content.html"
    fields = ['content']
    success_url = reverse_lazy('gestion:index')

    def get_object(self):
        self.page_user = get_object_or_404(User, username=self.args[0])
        self.template = get_object_or_404(LessonTemplate, num=self.args[1], year=self.page_user.profil.year)
        return get_object_or_404(Lesson, author=self.page_user, template=self.template)

class AjaxLessonUpdateRemarks(UpdateView, PermissionRequiredMixin):
    # permission
    permission_required = 'oral.change_lesson'
    # arg 0 : username
    # arg 1 : lesson number
    template_name = "oral/ajax/lesson_update_remarks.html"
    fields = ['remarks']
    success_url = reverse_lazy('gestion:index')

    def get_object(self):
        self.page_user = get_object_or_404(User, username=self.args[0])
        self.template = get_object_or_404(LessonTemplate, num=self.args[1], year=self.page_user.profil.year)
        return get_object_or_404(Lesson, author=self.page_user, template=self.template)


class AjaxLessonShowField(View):
    def get(self, request, username, template_num, field_name):
        page_user = get_object_or_404(User, username=username)
        template = get_object_or_404(LessonTemplate, num=template_num, year=page_user.profil.year)
        lesson = get_object_or_404(Lesson, author=page_user, template=template)
        field = getattr(lesson, field_name)
        return render(request, "oral/ajax/lesson_%s.html" % field_name, {'field': field})


class AjaxLessonShowTOC(View):
    def get(self, request, username, template_num):
        page_user = get_object_or_404(User, username=username)
        template = get_object_or_404(LessonTemplate, num=template_num, year=page_user.profil.year)
        lesson = get_object_or_404(Lesson, author=page_user, template=template)
        return render(request, "oral/ajax/lesson_toc.html", {'lesson': lesson})

# class ReferenceList(ListView):
#     model = Reference
#     template_name = "agreg/ref_list.html"
#     context_object_name = 'ref_list'
# 
# 
# class ReferenceDetail(DetailView):
#     model = Reference
#     template_name = "agreg/ref_detail.html"
