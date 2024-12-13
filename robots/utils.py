from io import BytesIO

from django.http import JsonResponse
from openpyxl import Workbook


def create_json_response(message, data=None, status=200):
    response = {"message": message}
    if data:
        response.update(data)
    return JsonResponse(response, status=status)


def create_excel_file(data, sheet_title="Summary"):
    wb = Workbook()
    ws = wb.active
    ws.title = sheet_title
    ws.append(["Модель", "Версия", "Количество за неделю"])
    for item in data:
        ws.append([item["model"], item["version"], item["total"]])
    file_stream = BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)
    return file_stream
