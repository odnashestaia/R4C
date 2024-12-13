from django.urls import path

from .views import create_robot, generate_summary_report

urlpatterns = [
    path('create/', create_robot, name='create'),
    path("summary/", generate_summary_report, name="summary"),
]
