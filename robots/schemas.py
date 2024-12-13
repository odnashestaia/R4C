from datetime import datetime

from pydantic import BaseModel, Field


class RobotSchema(BaseModel):
    model: str = Field(max_length=2,
                       description="Model name (max 2 characters)")
    version: str = Field(max_length=2,
                         description="Version name (max 2 characters)")
    created: datetime
