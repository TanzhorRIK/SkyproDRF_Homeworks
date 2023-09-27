from rest_framework import serializers
from course.models import Course, Lesson, Payments
from course.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    validators = [UrlValidator(field='video_url')]
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    validators = [UrlValidator(field='video_url')]
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lessons = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return obj.lesson_set.all().count()

    def get_lessons(self, obj):
        """Добавление уроков для курса"""
        lesson_list = []
        if obj.lesson_set.all():
            for i in obj.lesson_set.all().values_list():
                lesson_list.append("Название:" + i[2])
            return lesson_list
        return None


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'
