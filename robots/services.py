from datetime import datetime

from django.db.models import Count
from django.utils.timezone import make_aware, utc

from .models import Robot


def get_robot_summary():
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=7)

    start_date = make_aware(start_date, utc)
    end_date = make_aware(end_date, utc)
    return (
        Robot.objects.filter(created__range=[start_date, end_date])
        .values("model", "version")
        .annotate(total=Count("id"))
    )


def create_robot_in_db(validated_data):
    return Robot.objects.create(
        model=validated_data["model"],
        version=validated_data["version"],
        created=validated_data["created"]
    )
