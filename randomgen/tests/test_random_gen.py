"""Unit tests for randomgen library using system clock cycles."""

import unittest

from randomgen.generators import (
    TimestampRandomGenerator,
    ClockCycleRandomGenerator,
)
from randomgen.utils import (
    generate_random,
    generate_random_float,
    generate_random_clock,
    generate_random_float_clock,
)


class TestClockCycleRandomGenerator(unittest.TestCase):
    """Tests for clock-cycle based random generator."""

    def setUp(self):
        self.gen = ClockCycleRandomGenerator(max_value=100, min_value=0)

    def test_clock_random_returns_float_0_to_1(self):
        result = self.gen.random()
        self.assertGreaterEqual(result, 0)
        self.assertLess(result, 1)

    def test_clock_randint_in_range(self):
        result = self.gen.randint()
        self.assertGreaterEqual(result, 0)
        self.assertLess(result, 100)

    def test_clock_randint_range(self):
        result = self.gen.randint_range(25, 75)
        self.assertGreaterEqual(result, 25)
        self.assertLess(result, 75)

    def test_clock_random_float_range(self):
        result = self.gen.random_float_range(0.0, 1.0)
        self.assertGreaterEqual(result, 0.0)
        self.assertLess(result, 1.0)


class TestClockConvenienceFunctions(unittest.TestCase):
    """Tests for clock-based convenience functions."""

    def test_generate_random_clock(self):
        result = generate_random_clock(max_value=30, min_value=5)
        self.assertGreaterEqual(result, 5)
        self.assertLess(result, 30)

    def test_generate_random_float_clock(self):
        result = generate_random_float_clock()
        self.assertGreaterEqual(result, 0)
        self.assertLess(result, 1)


class TestDifferentValuesGenerated(unittest.TestCase):
    """Tests that different inputs produce different outputs."""

    def test_rapid_calls_produce_different_values(self):
        gen = ClockCycleRandomGenerator()
        values = [gen.random() for _ in range(10)]
        unique_count = sum(1 for i in range(len(values))
                          for j in range(i+1, len(values))
                          if abs(values[i] - values[j]) >= 1e-9)
        self.assertGreater(unique_count, 0)

    def test_high_frequency_samples_unique(self):
        gen = ClockCycleRandomGenerator()
        for _ in range(10):
            gen.random()
        values = [gen.random() for _ in range(50)]
        rounded = set(round(v, 8) for v in values)
        self.assertEqual(len(rounded), len(values))


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""

    def test_zero_range(self):
        gen = ClockCycleRandomGenerator(max_value=0, min_value=0)
        result = gen.randint()
        self.assertEqual(result, 0)


class TestIntegration(unittest.TestCase):
    """Integration tests comparing both generators."""

    def test_api_compatibility(self):
        ts_gen = TimestampRandomGenerator(100, 0)
        clock_gen = ClockCycleRandomGenerator(100, 0)
        
        ts_random = ts_gen.random()
        clock_random = clock_gen.random()
        ts_int = ts_gen.randint()
        clock_int = clock_gen.randint()
        
        self.assertLess(ts_random, 1)
        self.assertGreaterEqual(ts_int, 0)
        self.assertLess(clock_random, 1)


class TestModuleImports(unittest.TestCase):
    """Tests verifying module exports."""

    def test_import_both_generators(self):
        from randomgen import TimestampRandomGenerator, ClockCycleRandomGenerator
        self.assertIsInstance(TimestampRandomGenerator, type)
        self.assertIsInstance(ClockCycleRandomGenerator, type)

    def test_convenience_functions_callable(self):
        from randomgen import generate_random, generate_random_float
        self.assertTrue(callable(generate_random))
        self.assertTrue(callable(generate_random_float))


if __name__ == "__main__":
    unittest.main()
