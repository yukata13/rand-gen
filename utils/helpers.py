"""Convenience functions for quick random number generation without instantiation."""

from typing import Union, Callable

from randomgen.generators.timestamp_generator import TimestampRandomGenerator
from randomgen.generators.clock_generator import ClockCycleRandomGenerator


def generate_random(
    max_value: int = 100, 
    min_value: int = 0,
    use_clock_cycles: bool = False
) -> int:
    """Generate a single random integer.
    
    Convenience function that internally creates and uses the appropriate
    generator based on the use_clock_cycles parameter.
    
    Args:
        max_value: Maximum value for random generation (exclusive)
        min_value: Minimum value for random generation (inclusive)
        use_clock_cycles: If True, uses CPU clock cycles instead of timestamp
        
    Returns:
        Random integer in the specified range [min_value, max_value).
    
    Example:
        >>> from randomgen import generate_random
        >>> num = generate_random(50)  # Returns int between 0-49
        >>> print(num)
        23
    """
    if use_clock_cycles:
        generator = ClockCycleRandomGenerator(max_value=max_value, min_value=min_value)
    else:
        generator = TimestampRandomGenerator(max_value=max_value, min_value=min_value)
    
    return generator.randint()


def generate_random_float(
    max_value: float = 1.0, 
    min_value: float = 0.0,
    use_clock_cycles: bool = False
) -> float:
    """Generate a single random float between two values.
    
    Convenience function that internally creates and uses the appropriate
    generator based on the use_clock_cycles parameter.
    
    Args:
        max_value: Maximum value for random generation (exclusive)
        min_value: Minimum value for random generation (inclusive)
        use_clock_cycles: If True, uses CPU clock cycles instead of timestamp
        
    Returns:
        Random float in the range [min_value, max_value).
    
    Example:
        >>> from randomgen import generate_random_float
        >>> num = generate_random_float()  # Returns float between 0-1
        >>> print(f"{num:.6f}")
        0.847293
    """
    if use_clock_cycles:
        generator = ClockCycleRandomGenerator(max_value=max_value, min_value=min_value)
    else:
        generator = TimestampRandomGenerator(max_value=max_value, min_value=min_value)
    
    # Call random_float_range directly to get a float in range
    return generator.random_float_range(min_value, max_value)


def generate_random_clock(
    max_value: int = 100, 
    min_value: int = 0
) -> int:
    """Generate a single random integer using clock cycles.
    
    Wrapper around generate_random() with use_clock_cycles=True.
    
    Args:
        max_value: Maximum value for random generation (exclusive)
        min_value: Minimum value for random generation (inclusive)
        
    Returns:
        Random integer in the specified range [min_value, max_value)
        generated using CPU clock cycles as entropy source.
    
    Example:
        >>> from randomgen import generate_random_clock
        >>> num = generate_random_clock(30, 5)  # Returns int between 5-29
        >>> print(num)
        17
    """
    generator = ClockCycleRandomGenerator(max_value=max_value, min_value=min_value)
    return generator.randint()


def generate_random_float_clock(
    max_value: float = 1.0, 
    min_value: float = 0.0
) -> float:
    """Generate a single random float between 0 and 1 using clock cycles.
    
    Wrapper around generate_random_float() with use_clock_cycles=True.
    
    Args:
        max_value: Maximum value for random generation (exclusive, default 1.0)
        min_value: Minimum value for random generation (inclusive, default 0.0)
        
    Returns:
        Random float between min_value and max_value generated using CPU 
        clock cycles as entropy source.
    
    Example:
        >>> from randomgen import generate_random_float_clock
        >>> num = generate_random_float_clock()  # Returns float between 0-1
        >>> print(f"{num:.6f}")
        0.923847
    """
    generator = ClockCycleRandomGenerator(max_value=max_value, min_value=min_value)
    return generator.random_float_range(min_value, max_value)
