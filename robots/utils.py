from django.http import JsonResponse


def create_json_response(message, data=None, status=200):
    response = {"message": message}
    if data:
        response.update(data)
    return JsonResponse(response, status=status)
