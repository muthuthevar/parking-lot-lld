from abc import ABC, abstractmethod

from enums import SpotType, VehicleType


class Vehicle(ABC):
    def __init__(self, license_plate: str):
        self.license_plate = license_plate
        self.vehicle_type = self.get_vehicle_type()

    @abstractmethod
    def get_vehicle_type(self) -> VehicleType:
        pass

    @abstractmethod
    def get_required_spot_type(self) -> SpotType:
        pass

    def __str__(self) -> str:
        return f"{self.vehicle_type.value} - {self.license_plate}"


class Car(Vehicle):
    def get_vehicle_type(self) -> VehicleType:
        return VehicleType.CAR

    def get_required_spot_type(self) -> SpotType:
        return SpotType.REGULAR


class Motorcycle(Vehicle):
    def get_vehicle_type(self):
        return VehicleType.MOTORCYCLE

    def get_required_spot_type(self) -> SpotType:
        return SpotType.COMPACT


class Truck(Vehicle):
    def get_vehicle_type(self) -> VehicleType:
        return VehicleType.TRUCK

    def get_required_spot_type(self) -> SpotType:
        return SpotType.LARGE
