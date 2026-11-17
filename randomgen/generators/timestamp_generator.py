"""Timestamp-based random number generator."""

from randomgen.generators.base import BaseRandomGenerator


class TimestampRandomGenerator(BaseRandomGenerator):
    """A random number generator that uses current system timestamp.
    
    Uses the current Unix timestamp combined with a hash to generate
    pseudo-random numbers. This provides a deterministic but unpredictable
    seed based on time.
    
    Note: This generator is best used in single-threaded applications or
    when entropy from wall-clock time is sufficient for your use case.
    """
    
    def __init__(self, max_value: int = 100, min_value: int = 0):
        """Initialize the timestamp-based random number generator.
        
        Args:
            max_value: Maximum value for random generation (exclusive)
            min_value: Minimum value for random generation (inclusive)
        """
        super().__init__(max_value=max_value, min_value=min_value)
        self._last_timestamp = None
    
    def _get_entropy_source(self) -> float:
        """Get current timestamp with high resolution.
        
        Combines seconds and microseconds for better granularity.
        
        Returns:
            A tuple of (seconds, microseconds) as a single numeric value.
        """
        import datetime
        
        self._last_timestamp = datetime.datetime.now()
        now = self._last_timestamp
        # Create timestamp string with high precision
        timestamp_str = f"{int(now.timestamp())}.{now.microsecond:06d}"
        return float(timestamp_str)
    
    def random(self) -> float:
        """Generate a single random float between 0 and 1.
        
        Updates the internal timestamp state before generating randomness.
        
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
        
        Updates the internal timestamp state before generating randomness.
        
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
