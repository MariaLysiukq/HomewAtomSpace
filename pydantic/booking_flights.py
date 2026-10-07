from pydantic import BaseModel, EmailStr, field_validator, model_validator
from pydantic import Field


class Passenger(BaseModel):
    first_name: str
    last_name: str
    age: int
    is_child: bool=False

    
    @field_validator("age")
    def validate_age(cls, value):
        if value < 0 or value > 120:
            raise ValueError("Your age must be from 0 to 120")
        return value
        
        
    @model_validator(mode="after")
    def set_is_child(self):
        if self.age < 18:
            self.is_child = True
        return self
    
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Flight(BaseModel):
    flight_number: str
    origin: str
    destination: str
    price: float
    
    
    @field_validator("price")
    def validate_price(cls, value: float):
        if value < 0:
            raise ValueError("Price cannot be less than 0")
        return value


    @model_validator(mode="after")
    def validate_origin(self):
        if self.origin == self.destination:
            raise ValueError("you cannot fligth from the place you are")
        return self


    @property
    def route(self):
        return f"{self.origin} -> {self.destination}"


class Ticket(BaseModel):
    passenger: Passenger
    flight: Flight
    seat_number: int
    has_baggage: bool=False
    
    
    @field_validator("seat_number")
    def validate_seat_number(cls, value) -> int:
        if value < 1 or value > 200:
            raise ValueError("We don't have this seat, pick the seat between 1 and 200")
        return value
        
        
    @model_validator(mode="after")
    def validate_emergency_seating(self):
        if self.passenger.is_child and self.seat_number in [13, 14]:
            raise ValueError("This is an emergency row; a child cannot sit in seats 13 or 14")
        return self
    
    @property
    def total_price(self) -> float:
        total = self.flight.price
        if self.has_baggage:
            return total + 50
        return total

        
ticket = Ticket(
    passenger={"first_name": "Maria", "last_name": "Lysiuk", "age": 18},
    flight={"flight_number": "fo2u3f", "origin": "WOW", "destination": "WAW", "price": 1000000000},
    seat_number=13,
    has_baggage=True,
)

print(ticket.passenger.full_name)
print(ticket.flight.route)
print(ticket.total_price) 
