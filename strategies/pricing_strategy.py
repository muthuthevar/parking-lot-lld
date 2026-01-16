from abc import ABC, abstractmethod
import datetime


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, entry_time: datetime, exit_time: datetime) -> float:
        pass


class HourlyPricingStrategy(PricingStrategy):
    def __init__(self, rate_per_hour: float = 2.0, minimum_hours: float = 1.0):
        self.rate_per_hour = rate_per_hour
        self.minimum_hours = minimum_hours

    def calculate_fee(self, entry_time: datetime, exit_time: datetime) -> float:
        duration = exit_time - entry_time
        hours = duration.total_seconds() / 3600.0

        hours = max(hours, self.minimum_hours)
        hours = int(hours) + (1 if hours % 1 > 0 else 0)
        return hours * self.rate_per_hour


class FlatRatePricingStrategy(PricingStrategy):
    def __init__(self, flat_rate: float = 5.0):
        self.flat_rate = flat_rate

    def calculate_fee(self, entry_time: datetime, exit_time: datetime) -> float:
        return self.flat_rate
