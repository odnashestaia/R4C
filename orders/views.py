import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from robots.models import Robot

from .models import Order


@csrf_exempt
def create_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            customer_id = data.get("customer_id")
            robot_serial = data.get("robot_serial")

            # Проверяем, что переданы все необходимые данные
            if not customer_id or not robot_serial:
                return JsonResponse({"error": "Необходимо указать customer_id и robot_serial"}, status=400)

            robot = Robot.objects.filter(serial=robot_serial).first()

            if robot:
                return JsonResponse({
                    "message": f"Робот уже доступен: {robot.model}, версия {robot.version}."
                }, status=200)

            order = Order.objects.create(
                customer_id=customer_id,
                robot_serial=robot_serial
            )
            return JsonResponse({"message": "Заказ успешно создан", "order_id": order.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Некорректный JSON формат"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Метод не поддерживается"}, status=405)
