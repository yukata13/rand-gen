# Timestamp Random Generator Library 🎲

This is a personal learning project for using local llms with VsCode; Almost all of the code here are written by AI:

A lightweight Python library that generates pseudo-random numbers using system timestamps and CPU clock cycles as entropy sources. Uses SHA-256 hashing to convert time-based data into high-quality random values.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
This
> 🤖 **Developed with Cline + Ollama + Qwen3.5:9b**

## ✨ Features

- **Two Entropy Sources**: Timestamp-based or CPU clock cycle-based random generation
- **SHA-256 Hashing**: Cryptographic hashing for unpredictable outputs
- **Multiple Output Types**: Integers, floats, custom ranges
- **Easy Integration**: Class-based and function-based approaches
- **Cross-Platform**: Windows, macOS, Linux compatible

## 🚀 Quick Start

### Installation (Local Only - Not on PyPI)

**⚠️ This package is NOT published on PyPI. Install from source directly:**

Clone from the GitHub repository:

```bash
git clone https://github.com/yukata13/rand-gen.git
cd rand-gen
python -m pip install -e .
```

Or install from your local path in another project:

```bash
pip install -e /path/to/rand-gen
```

Note: The `pip install -e .` creates an editable installation that uses the files directly from your cloned repository. No PyPI download is involved.

### Basic Usage

```python
from randomgen import TimestampRandomGenerator, ClockCycleRandomGenerator

# Using timestamp-based generator (default)
ts_gen = TimestampRandomGenerator(max_value=100, min_value=0)
number = ts_gen.randint()  # Random int 0-99
print(number)

# Using CPU clock cycle-based generator
clock_gen = ClockCycleRandomGenerator(max_value=100, min_value=0)
clock_number = clock_gen.randint()
print(clock_number)
```

### Convenience Functions

```python
from randomgen import generate_random, generate_random_float, generate_random_clock

# Quick integer generation
num = generate_random(50)  # Returns int between 0-49
print(num)

# Using clock cycles
clock_num = generate_random_clock(30, 5)  # 5-29
print(clock_num)
```

### Custom Ranges

```python
gen = TimestampRandomGenerator()
int_val = gen.randint_range(100, 200)  # 100-199
float_val = gen.random_float_range(-1.0, 1.0)  # -1.0 to 1.0
```

## 🔧 API Reference

### TimestampRandomGenerator

Uses system wall-clock timestamp with microseconds as entropy source.

**Parameters:**
- `max_value` (int): Maximum value (exclusive), default=100
- `min_value` (int): Minimum value (inclusive), default=0

**Methods:**
- `random()` → `float`: Random float in [0, 1)
- `randint()` → `int`: Random integer in range
- `randint_range(min_val, max_val)` → `int`: Custom int range
- `random_float_range(min_val, max_val)` → `float`: Custom float range

### ClockCycleRandomGenerator

Uses high-resolution CPU performance counter (thread_time_ns on Python 3.12+, perf_counter otherwise). Preferred for multi-threaded applications.

**Parameters & Methods:** Same as TimestampRandomGenerator

### Module-Level Functions

| Function | Description |
|----------|-------------|
| `generate_random(max_value, min_value=0)` | Random int using timestamp |
| `generate_random_float(max_value, min_value=0.0)` | Random float 0-1 |
| `generate_random_clock(max_value, min_value=0)` | Clock-based random int |
| `generate_random_float_clock(max_value, min_value=0.0)` | Clock-based random float |

## 🧪 Testing

```bash
cd tests
python -m pytest test_random_gen.py
# Or using unittest:
python test_random_gen.py
```

Tests cover: Basic generation, range boundaries, multi-threaded entropy, API compatibility, imports.

## 🔮 Future Enhancements

- Seeded random generator
- Cryptographically secure RNG (CSPRNG)
- Configurable hash algorithms
- Batch generation
- Async-compatible generators

## 🐛 Troubleshooting

**Same values rapidly**: Add delay or use ClockCycleRandomGenerator for CPU cycle entropy instead.

**Not updating**: Call `randint()` or `random()` - they internally update the entropy source.

## 🤝 Contributing

See CONTRIBUTING.md for guidelines.

## 📜 License

MIT License - see LICENSE file.

## 👥 Author

Yukata13