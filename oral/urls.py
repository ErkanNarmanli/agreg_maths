from django.conf.urls import url, include

from .views import LessonDetail, LessonList

app_name = 'oral'

urlpatterns = [
        url(r'([\w-]+)/lessons/$', LessonList.as_view(), name='lessons'),
        url(r'([\w-]+)/([0-9]+)/$', LessonDetail.as_view(), name='detail'),
]
        
