# Changelog

All notable changes to the Timestamp Random Generator Library will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of Timestamp Random Generator Library
- TimestampRandomGenerator class with timestamp-based entropy source
- ClockCycleRandomGenerator class with CPU cycle counter entropy source
- Module-level convenience functions (generate_random, generate_random_float, etc.)
- Comprehensive unit test suite
- Full documentation with README.md

### Changed
- None yet

### Deprecated
- None yet

### Removed
- None yet

## [0.1.0] - YYYY-MM-DD

### Added
- TimestampRandomGenerator class
- ClockCycleRandomGenerator class (supports Python 3.8+)
- Convenience functions:
  - generate_random() - Integer generation using timestamp
  - generate_random_float() - Float generation using timestamp
  - generate_random_clock() - Integer generation using CPU cycles
  - generate_random_float_clock() - Float generation using CPU cycles
- Custom range methods:
  - randint_range(min_val, max_val)
  - random_float_range(min_val, max_val)

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

## [0.1.1] (Future)

### Planned
- Add seeded random generator for reproducible sequences
- Add cryptographically secure random number generator option
- Configurable hash algorithm (SHA-256, SHA-3, BLAKE2)
- Batch generation methods for performance
- Async-compatible generators with asyncio.run() support

## [0.2.0] (Future)

### Planned
- Integration tests with pytest
- Coverage reports with coverage.py
- PyPI package publication
- Docker container image