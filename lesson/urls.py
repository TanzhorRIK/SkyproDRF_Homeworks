from lesson.apps import LessonConfig
from django.urls import path

from lesson.views import LessonCreateAPIView, LessonListAPIView, \
    LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView

app_name = LessonConfig.name


urlpatterns = [
    path('create/', LessonCreateAPIView.as_view(), name='create_lesson'),
    path('list/', LessonListAPIView.as_view(), name='list_lesson'),
    path('list/<int:pk>/', LessonRetrieveAPIView.as_view(), name='get_lesson'),
    path('list/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update_lesson'),
    path('list/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete_lesson'),
]