from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ParticipantCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=2, max_length=50)
    email: EmailStr


class Participant(ParticipantCreate):
    id: int


class EventCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=10, max_length=120)
    location: str = Field(min_length=20, max_length=200)
    event_date: date
    capacity: int = Field(ge=1, le=1000, strict=True)


class Event(EventCreate):
    id: int
    participants: list[Participant] = Field(default_factory=list)
