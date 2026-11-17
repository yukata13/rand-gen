"""
RandomGen - A library for generating pseudo-random numbers.

This package provides multiple random number generation strategies:
- Timestamp-based generator (wall-clock time entropy)
- Clock cycle-based generator (CPU cycle counter entropy)

Usage examples:
    from randomgen import TimestampRandomGenerator, ClockCycleRandomGenerator
    gen = TimestampRandomGenerator()
    num = gen.randint()

Module-level convenience functions:
    from randomgen import generate_random, generate_random_float
    num = generate_random(100)  # Returns int between 0-99
"""

# Import and expose public API
from .generators.timestamp_generator import TimestampRandomGenerator
from .generators.clock_generator import ClockCycleRandomGenerator
from .utils.helpers import (
    generate_random,
    generate_random_float,
    generate_random_clock,
    generate_random_float_clock,
)

__all__ = [
    "TimestampRandomGenerator",
    "ClockCycleRandomGenerator",
    "generate_random",
    "generate_random_float",
    "generate_random_clock",
    "generate_random_float_clock",
]