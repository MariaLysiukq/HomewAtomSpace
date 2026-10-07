from fastapi import APIRouter, HTTPException, status

from app.models.events import Event, EventCreate, Participant, ParticipantCreate
from ._detail.json import read_json, write_json, database_lock


router = APIRouter(tags=["Events"])


def _find_event(events, event_id):
    for event in events:
        if event["id"] == event_id:
            return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Подію не знайдено")


@router.get("/api/events", response_model=list[Event])
def get_events():
    with database_lock:
        return read_json()["events"]


@router.post("/api/events", response_model=Event, status_code=status.HTTP_201_CREATED)
def create_event(payload: EventCreate) -> Event:
    with database_lock:
        data = read_json()
        new_event = Event(id=len(data["events"]) + 1, participants=[], **payload.model_dump())
        data["events"].append(new_event.model_dump(mode="json"))
        write_json(data)
        return new_event
