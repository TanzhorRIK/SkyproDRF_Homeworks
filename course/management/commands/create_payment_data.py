from django.core.management import BaseCommand

from course.models import Payments
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        Pay_1 = Payments.objects.create(
            user=User.objects.get(email='tanzhor4@yandex.ru'),
            type_metod='Course',
            sum_pay=25000.00,
            payment_method='Cash'

        )
        Pay_1.save()
        Pay_2 = Payments.objects.create(
            user=User.objects.get(email='test1@test.ru'),
            type_metod='Lesson',
            sum_pay=1600.95,
            payment_method='Account_transfer'

        )
        Pay_2.save()
        Pay_3 = Payments.objects.create(
            user=User.objects.get(email='test2@test.ru'),
            type_metod='Lesson',
            sum_pay=6000,
            payment_method='Account_transfer'

        )
        Pay_3.save()