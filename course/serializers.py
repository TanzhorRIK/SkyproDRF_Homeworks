from rest_framework import serializers
from course.models import Course, Lesson, Payments, Subscription
from course.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    validators = [UrlValidator(field='video_url')]

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    validators = [UrlValidator(field='video_url')]
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    subscription = serializers.SerializerMethodField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.get('context').get('request')

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

    def get_subscription(self, instance):
        user = self.request.user
        sub_all = instance.subscription.all()
        for sub in sub_all:
            if sub.subscriber == user:
                return True
        return False



class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
