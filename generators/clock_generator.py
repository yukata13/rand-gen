"""Clock cycle-based random number generator."""

import time

from randomgen.generators.base import BaseRandomGenerator


class ClockCycleRandomGenerator(BaseRandomGenerator):
    """A random number generator that uses system CPU clock cycles as reference.
    
    Uses the high-resolution performance counter to generate pseudo-random 
    numbers based on CPU cycles/hertz. This provides a fast and hardware-based
    source of randomness.
    
    Note: In Python 3.12+, consider using thread_time_ns() instead for better
    multi-threaded entropy distribution (see docstring in _get_entropy_source()).
    
    For older Python versions, perf_counter() is used universally.
    """
    
    def __init__(self, max_value: int = 100, min_value: int = 0):
        """Initialize the clock cycle-based random number generator.
        
        Args:
            max_value: Maximum value for random generation (exclusive)
            min_value: Minimum value for random generation (inclusive)
        """
        super().__init__(max_value=max_value, min_value=min_value)
        self._last_cycle_count = None
    
    def _get_entropy_source(self) -> float:
        """Get current high-resolution counter value.
        
        In Python 3.12+, prefers thread_time_ns() for multi-threaded awareness.
        Falls back to perf_counter() for older Python versions or single-threaded apps.
        
        Returns:
            The current counter value in seconds (for backward compatibility with base class).
        """
        # Try thread_time_ns first (Python 3.12+) for better multi-threaded safety
        if hasattr(time, 'thread_time_ns'):
            self._last_cycle_count = time.thread_time_ns() / 1e9  # Convert to seconds
            return self._last_cycle_count
        
        # Fall back to perf_counter for older Python or single-threaded apps
        self._last_cycle_count = time.perf_counter()
        return self._last_cycle_count
    
    def random(self) -> float:
        """Generate a single random float between 0 and 1.
        
        Updates the internal counter state before generating randomness.
        
        Returns:
            A float between 0 (inclusive) and 1 (exclusive).
        """
        entropy_value = self._get_entropy_source()
        hash_value = self._generate_hash(entropy_value)
        # Take first few characters of hex digest for randomness
        random_bytes = int(hash_value[:8], 16) / 2**32
        return random_bytes
    
    def randint(self) -> int:
        """Generate a single random integer in the specified range.
        
        Updates the internal counter state before generating randomness.
        
        Returns:
            An integer between min_value and max_value 
            (inclusive of min, exclusive of max).
        """
        entropy_value = self._get_entropy_source()
        hash_value = self._generate_hash(entropy_value)
        random_bytes = int(hash_value[:8], 16) / 2**32
        # Scale to range and convert to int
        value = self.min_value + int(random_bytes * (self.max_value - self.min_value))
        return value
    
    def randint_range(self, min_val: int, max_val: int) -> int:
        """Generate a random integer in a custom range.
        
        Args:
            min_val: Minimum value (inclusive)
            max_val: Maximum value (exclusive)
            
        Returns:
            Random integer between min_val and max_val.
        """
        entropy_value = self._get_entropy_source()
        hash_value = self._generate_hash(entropy_value)
        random_bytes = int(hash_value[:8], 16) / 2**32
        value = min_val + int(random_bytes * (max_val - min_val))
        return value
    
    def random_float_range(self, min_val: float, max_val: float) -> float:
        """Generate a random float in a custom range.
        
        Args:
            min_val: Minimum value (inclusive)
            max_val: Maximum value (exclusive)
            
        Returns:
            Random float between min_val and max_val.
        """
        entropy_value = self._get_entropy_source()
        hash_value = self._generate_hash(entropy_value)
        random_bytes = int(hash_value[:8], 16) / 2**32
        return min_val + random_bytes * (max_val - min_val)
