"""Base class for all random number generators."""

import time
import hashlib


class BaseRandomGenerator:
    """Abstract base class for random number generators.
    
    All generators should inherit from this class and implement:
    - _get_entropy_source(): Returns the entropy source value
    - _generate_hash(entropy): Converts entropy to a hash
    
    Public methods (implemented by subclasses):
    - random(): Generate float in [0, 1)
    - randint(): Generate integer in [min_value, max_value)
    - randint_range(min_val, max_val): Generate int in custom range
    - random_float_range(min_val, max_val): Generate float in custom range
    """
    
    def __init__(self, max_value: int = 100, min_value: int = 0):
        """Initialize the random number generator.
        
        Args:
            max_value: Maximum value for random generation (exclusive)
            min_value: Minimum value for random generation (inclusive)
        """
        self.max_value = max_value
        self.min_value = min_value
    
    def _get_entropy_source(self) -> float:
        """Get the entropy source value.
        
        Subclasses must implement this method to provide a unique
        entropy value (e.g., timestamp, clock cycle count).
        
        Returns:
            A numeric value representing the current entropy source state.
        """
        raise NotImplementedError("Subclasses must implement _get_entropy_source()")
    
    def _generate_hash(self, entropy_value: float) -> str:
        """Generate a hash from an entropy value.
        
        Args:
            entropy_value: The entropy source value to hash.
            
        Returns:
            Hexadecimal string representation of the hash.
        """
        # Convert entropy value to string for hashing
        entropy_str = f"{entropy_value:.10f}"
        return hashlib.sha256(entropy_str.encode()).hexdigest()
    
    def random(self) -> float:
        """Generate a single random float between 0 and 1.
        
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
        
        Returns:
            An integer between min_value and max_value 
            (inclusive of min, exclusive of max).
        """
        random_float = self.random()
        # Scale to range and convert to int
        value = self.min_value + int(random_float * (self.max_value - self.min_value))
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
