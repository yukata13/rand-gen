# Contributing to RandomGen Library

Thank you for your interest in contributing to the Timestamp Random Generator Library! This document outlines how to contribute.

## 📋 Code of Conduct

Please be respectful and professional in all interactions. We welcome diverse contributions from all backgrounds.

## 🛠️ Getting Started

### Development Setup

```bash
# Clone the repository
git clone https://github.com/yukata13/rand-gen.git
cd randomgen

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies and in development mode
pip install -e ".[dev]"
```

### Run Tests

```bash
# Run all tests
pytest randomgen/tests/

# Or run with unittest
python randomgen/tests/test_random_gen.py
```

## 📝 Development Guidelines

### Code Style

- Use **black** for code formatting (line length 88)
- Use **flake8** for linting
- Follow PEP 8 conventions
- Add type hints where appropriate

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new feature
fix: bug fix
docs: documentation changes
style: code style changes
refactor: code refactoring
test: test additions/modifications
chore: maintenance tasks
```

### Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure nothing breaks
5. Commit your changes
6. Push to the branch
7. Open a Pull Request

### Review Process

- All PRs will be reviewed by maintainers
- Address feedback in discussion threads
- Keep PRs focused and small when possible
- Tests must pass before merging

## 🧪 Adding Tests

When adding new features, include tests:

```python
# Example test structure
class TestNewFeature(unittest.TestCase):
    def test_feature_works(self):
        """Test that the feature works correctly"""
        # Your test code here
        pass
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions"""
        # Your edge case tests here
        pass
```

## 🌟 Areas Needing Contribution

### Priority Issues

- [ ] Add integration tests with third-party libraries
- [ ] Add documentation examples to README
- [ ] Performance optimization for high-frequency generation
- [ ] Add more entropy sources (e.g., noise from hardware)

### Good First Issues

- [ ] Update documentation
- [ ] Fix minor bugs
- [ ] Add code comments
- [ ] Improve error messages

## 📚 Documentation Guidelines

- Keep docs in sync with code changes
- Use clear, concise language
- Include practical examples
- Test examples before committing

## 🔧 Project Structure

```
randomgen/
├── generators/      # Core random generation logic
│   ├── base.py           # Base class
│   ├── timestamp_generator.py  # Timestamp-based
│   └── clock_generator.py     # Clock cycle-based
├── utils/              # Convenience functions
│   └── helpers.py
├── tests/              # Test suite
├── __init__.py        # Main exports
├── README.md          # Project documentation
├── LICENSE            # MIT license
└── CONTRIBUTING.md    # This file
```

## 🤝 Questions?

Feel free to open an issue or discussion for any questions. We're happy to help!

Thank you for contributing! 🎉