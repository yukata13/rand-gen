"""Timestamp Random Generator Library

A simple Python library that generates random numbers based on system timestamps.
Uses SHA-256 hashing to convert timestamp data into pseudo-random values.

Architecture:
├── generators/      - Contains all generator classes (timestamp, clock, base)
├── utils/           - Convenience functions for quick usage
└── tests/           - Unit test suite

Usage:
    from randomgen import TimestampRandomGenerator, generate_random
    
    gen = TimestampRandomGenerator(max_value=100)
    number = gen.randint()  # Random integer 0-99
    
    # Or use convenience functions:
    num = generate_random(50)      # Random int 0-49
    float_num = generate_random_float()  # Random float 0-1
"""

# Re-export public API from generators and utils modules
from randomgen.generators import TimestampRandomGenerator, ClockCycleRandomGenerator
from randomgen.utils import (
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
