import json

from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pydantic import ValidationError

from .models import Robot
from .shemas import RobotSchema


# #TODO отключить когда будет деплой
@csrf_exempt
def create_robot(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST requests are allowed.")

    try:
        # Парсим входящий JSON
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)

    try:
        # Валидация данных через Pydantic
        validated_data = RobotSchema(**data).dict()
    except ValidationError as e:
        return JsonResponse({"error": e.errors()}, status=400)
    # Сохранение данных в базу
    try:
        robot = Robot.objects.create(
            model=validated_data["model"],
            version=validated_data["version"],
            created=validated_data["created"]
        )
    except Exception as e:
        return JsonResponse({"error": f"Database error: {str(e)}"},
                            status=500)

    return JsonResponse({"message": "Robot created successfully",
                         "robot_id": robot.id}, status=201)
