import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from pydantic import ValidationError

from .schemas import RobotSchema
from .services import create_robot_in_db, get_robot_summary
from .utils import create_excel_file, create_json_response


def generate_summary_report(request):
    if request.method != "GET":
        return HttpResponseBadRequest("Only GET requests are allowed.")
    robot_data = get_robot_summary()
    file_stream = create_excel_file(robot_data)
    return HttpResponse(
        file_stream,
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


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
