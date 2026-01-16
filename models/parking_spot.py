from typing import Optional
from enums import SpotType
from models import Vehicle


class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: SpotType, floor_number: int = 1):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.floor_number = floor_number
        self.vehicle: Optional[Vehicle] = None

    @property()
    def is_occupied(self) -> bool:
        return self.vehicle is not None

    def park(self, vehicle: Vehicle) -> bool:
        if self.is_occupied:
            return False
        self.vehicle = vehicle
        return True

    def unpark(self) -> Optional[Vehicle]:
        if not self.is_occupied:
            return None
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle

    def can_accommodate(self, vehicle: Vehicle) -> bool:
        required_type = vehicle.get_required_spot_type()
        size_order = {SpotType.COMPACT: 1, SpotType.REGULAR: 2, SpotType.LARGE: 3}
        return size_order[self.spot_type] >= size_order[required_type]

    def __str__(self) -> str:
        status = f"Occupied by {self.vehicle}" if self.is_occupied else "Available"
        return f"Spot {self.spot_id} ({self.spot_type.value} - {status})"
