from django.conf.urls import url, include

from .views import LessonDetail, LessonList, LessonCreate, \
                AjaxLessonShowField, AjaxLessonUpdateContent, \
                AjaxLessonShowTOC, AjaxLessonUpdateRemarks, \
                DevList, DevDetail

app_name = 'oral'

urlpatterns = [
        url(r'developments/$', DevList.as_view(), name='devlist'),
        url(r'development/(?P<pk>[0-9]+)/$', DevDetail.as_view(), name='devdetail'),
        url(r'([\w-]+)/lessons/$', LessonList.as_view(), name='lessons'),
        url(r'([\w-]+)/([0-9]+)/$', LessonDetail.as_view(), name='detail'),
        url(r'([\w-]+)/([0-9]+)/create/$', LessonCreate.as_view(), name='create_lesson'),
        url(r'([\w-]+)/([0-9]+)/toc/$', AjaxLessonShowTOC.as_view(), name="ajax_lesson_toc"),
        url(r'([\w-]+)/([0-9]+)/([\w-]+)/$', AjaxLessonShowField.as_view(), name="ajax_lesson_field"),
        url(r'([\w-]+)/([0-9]+)/content/update/$', AjaxLessonUpdateContent.as_view(), name="ajax_lesson_update_content"),
        url(r'([\w-]+)/([0-9]+)/remarks/update/$', AjaxLessonUpdateRemarks.as_view(), name="ajax_lesson_update_remarks"),
]
        
