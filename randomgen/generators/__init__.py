"""Random number generator factory module."""

from .timestamp_generator import TimestampRandomGenerator
from .clock_generator import ClockCycleRandomGenerator

__all__ = [
    "TimestampRandomGenerator",
    "ClockCycleRandomGenerator",
]
