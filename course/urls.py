from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter
from django.urls import path
from course.views import (CourseViewSet, LessonCreateAPIView, LessonListAPIView,
                          LessonRetrieveAPIView, LessonUpdateAPIView,
                          LessonDestroyAPIView, PaymentsViewSet)

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'payments', PaymentsViewSet)
urlpatterns = [
                  path('create_lesson/', LessonCreateAPIView.as_view(),
                       name='create_lesson'),
                  path('list_lesson/', LessonListAPIView.as_view(),
                       name='list_lesson'),
                  path('list_lesson/<int:pk>/', LessonRetrieveAPIView.as_view(),
                       name='get_lesson'),
                  path('list_lesson/update/<int:pk>/',
                       LessonUpdateAPIView.as_view(),
                       name='update_lesson'),
                  path('list-lesson/delete/<int:pk>/',
                       LessonDestroyAPIView.as_view(),
                       name='delete_lesson'),
              ] + router.urls
