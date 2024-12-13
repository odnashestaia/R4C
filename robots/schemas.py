from datetime import datetime

from pydantic import BaseModel, Field


class RobotSchema(BaseModel):
    model: str = Field(max_length=2,
                       description="Model name (max 2 characters)")
    version: str = Field(max_length=2,
                         description="Version name (max 2 characters)")
    created: datetime

# from django.utils.dateparse import parse_datetime


# def validate_robot_data(data):
#     """
#     Функция для валидации данных робота.
#     """
#     # Проверка наличия обязательных полей
#     required_fields = {"model", "version", "created"}
#     missing_fields = required_fields - set(data.keys())
#     if missing_fields:
#         return {"error": f"Missing required fields: {missing_fields}"}

#     # Проверка длины полей model и version
#     if len(data.get("model", "")) > 2:
#         return {"error": "Model must be at most 2 characters long"}
#     if len(data.get("version", "")) > 2:
#         return {"error": "Version must be at most 2 characters long"}

#     # Проверка формата даты
#     created = parse_datetime(data.get("created", ""))
#     if created is None:
#         return {"error": "Invalid 'created' datetime format"}

#     # Возвращаем None, если ошибок нет
#     return None
