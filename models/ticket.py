import datetime
from typing import Optional
from models import Vehicle
from models.parking_spot import ParkingSpot


class Ticket:
    def __init__(self, ticket_id: str, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
        self.exit_time = Optional[datetime] = None

    def set_exit_time(self):
        self.exit_time = datetime.now()

    def get_duration_minutes(self):
        if self.exit_time is None:
            duration = datetime.now() - self.entry_time
        else:
            duration = self.exit_time - self.entry_time
        return duration.total_seconds() / 60.0

    def __str__(self) -> str:
        return f"Ticket id: {self.ticket_id} - {self.vehicle} at {self.spot.spot_id}"
