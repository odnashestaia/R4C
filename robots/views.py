import json

from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from pydantic import ValidationError

from .schemas import RobotSchema
from .services import create_robot_in_db
from .utils import  create_json_response


# #TODO отключить когда будет деплой
@csrf_exempt
def create_robot(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST requests are allowed.")

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return create_json_response("Invalid JSON format", status=400)

    try:
        validated_data = RobotSchema(**data).dict()
    except ValidationError as e:
        return create_json_response("Validation error",
                                    {"errors": e.errors()}, status=400)

    try:
        robot = create_robot_in_db(validated_data)
    except Exception as e:
        return create_json_response(f"Database error: {str(e)}", status=500)

    return create_json_response("Robot created successfully",
                                {"robot_id": robot.id}, status=201)
