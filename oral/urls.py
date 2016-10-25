from django.conf.urls import url, include

from .views import LessonDetail

app_name = 'oral'

urlpatterns = [
        url(r'([\w-]+)/([0-9]+)/$', LessonDetail.as_view(), name='detail'),
]
        
