from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from robots.models import Robot

from .models import Order


@receiver(post_save, sender=Robot)
def notify_customers_about_robot(sender, instance, created, **kwargs):
    """
    Уведомляет клиентов, если робот стал доступен и был добавлен в систему.
    """
    print('start sending')
    if created:  # Сигнал срабатывает только при создании робота
        pending_orders = Order.objects.filter(robot_serial=instance.serial)

        for order in pending_orders:
            customer = order.customer

            # Формируем письмо
            subject = "Ваш робот теперь доступен"
            message = (
                f"Добрый день!\n\n"
                f"Недавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}. "
                f"Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами."
            )

            # Отправляем письмо клиенту
            send_mail(
                subject,
                message,
                'no-reply@company.com',  # Отправитель
                [customer.email],  # Получатель
                fail_silently=False,
            )
