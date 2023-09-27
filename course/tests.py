from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Lesson
from course.paginators import CoursePaginator
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@mail.ru', password='12345', is_active=True)
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.data = {
            'name': 'подготовка ОГЭ',
            'description': 'Готовим быстро',
            'video_url': 'https://www.youtube.com/watch?v=HJAspAgHA4s',
            'owner': self.user.pk,
        }


    def test_create_lesson(self):
        """Создание урока тест"""
        url_lesson_create = reverse('course:create_lesson')
        response = self.client.post(url_lesson_create, self.data)
        data_response_true = {
            'id': response.json()['id'],
            'name': 'подготовка ОГЭ',
            'description': 'Готовим быстро',
            'image': None,
            'video_url': 'https://www.youtube.com/watch?v=HJAspAgHA4s',
            'course': None,
            'owner': self.user.pk
        }
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json(), data_response_true)
        self.assertTrue(Lesson.objects.all().exists())

    def test_read_lesson(self):
        """Чтение данных уроки тест"""
        url_lesson_create = reverse('course:create_lesson')
        response = self.client.post(url_lesson_create, self.data)
        lesson_id = response.json()['id']
        data_response_detail_true = {
            'id': lesson_id,
            'name': 'подготовка ОГЭ',
            'description': 'Готовим быстро',
            'image': None,
            'video_url': 'https://www.youtube.com/watch?v=HJAspAgHA4s',
            'course': None,
            'owner': self.user.pk
        }
        data_response_list_true = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [data_response_detail_true]
        }
        self.url_lesson_list = reverse('course:list_lesson')
        response = self.client.get(self.url_lesson_list)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        if Lesson.objects.all().count() > CoursePaginator.page_size:
            self.assertEquals(response.json(), data_response_list_true)
        else:
            self.assertEquals(response.json(), [data_response_detail_true])
        self.url_lesson_detail = reverse('course:get_lesson', kwargs={'pk': lesson_id})
        response = self.client.get(self.url_lesson_detail)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(), data_response_detail_true)

    def test_update_lesson(self):
        """Обновление данных уроки тест"""
        url_lesson_create = reverse('course:create_lesson')
        response = self.client.post(url_lesson_create, self.data)
        lesson_id = response.json()['id']
        data_response_update_put = {
            'name': 'Деньги 24',
            'description': 'Готовим быстро',
            'video_url': 'https://www.youtube.com/'
        }
        data_response_update_put_true = {
            'id': lesson_id,
            'name': 'Деньги 24',
            'description': 'Готовим быстро',
            'image': None,
            'video_url': 'https://www.youtube.com/',
            'course': None,
            'owner': self.user.pk
        }
        self.url_lesson_update = reverse('course:update_lesson', kwargs={'pk': lesson_id})
        response = self.client.put(self.url_lesson_update, data_response_update_put)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(), data_response_update_put_true)
        data_response_update_patch = {
            'description': 'test test'
        }
        data_response_update_patch_true = {
            'id': lesson_id,
            'name': 'Деньги 24',
            'description': 'test test',
            'image': None,
            'video_url': 'https://www.youtube.com/',
            'course': None,
            'owner': self.user.pk
        }
        response = self.client.patch(self.url_lesson_update, data_response_update_patch)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json(), data_response_update_patch_true)

    def test_delete_lesson(self):
        """Удаление данных уроки тест"""
        url_lesson_create = reverse('course:create_lesson')
        response = self.client.post(url_lesson_create, self.data)
        lesson_id = response.json()['id']
        self.url_lesson_delete = reverse('course:delete_lesson', kwargs={'pk': lesson_id})
        response = self.client.delete(self.url_lesson_delete)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.all().exists())


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:

        self.user1 = User.objects.create(email='test1@mail.ru', password='12345', is_active=True)
        self.user2 = User.objects.create(email='test2@mail.ru', password='12345', is_active=True)
        self.user1.save()
        self.user2.save()
        self.client.force_authenticate(user=self.user1)
        self.data_course = {
            'name': 'Разработчик Python',
            'description': 'Курс SkyPro',
            'video_url': 'https://www.youtube.com/watch?v=HJAspAgHA4s',
            'owner': self.user1.pk,
        }
        url_course_create = reverse('course:course-list')
        response = self.client.post(url_course_create, self.data_course)
        self.course_id = response.json()['id']

    def test_update_subscription(self):
        """Обновление подписки тест"""
        self.data_subscription = {
            'course': self.course_id,
            'subscriber': self.user2.pk,
        }
        url_subscription_create = reverse('course:subscription-list')
        response = self.client.post(url_subscription_create, self.data_subscription)
        # Проверка подписки user1
        self.client.force_authenticate(user=self.user1)
        url_course_detail = reverse('course:course-list')
        response = self.client.get(url_course_detail)
        self.assertFalse(response.json()[0]['subscription'])
        # Проверка подписки user2
        self.client.force_authenticate(user=self.user2)
        url_course_detail = reverse('course:course-list')
        response = self.client.get(url_course_detail)
        self.assertTrue(response.json()[0]['subscription'])
