from .models import Robot



def create_robot_in_db(validated_data):
    return Robot.objects.create(
        model=validated_data["model"],
        version=validated_data["version"],
        created=validated_data["created"],
        serial=f"{validated_data["model"]}-{validated_data["version"]}"
    )
