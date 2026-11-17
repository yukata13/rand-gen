"""Random number generator factory module."""

from randomgen.generators.timestamp_generator import TimestampRandomGenerator
from randomgen.generators.clock_generator import ClockCycleRandomGenerator

__all__ = [
    "TimestampRandomGenerator",
    "ClockCycleRandomGenerator",
]
