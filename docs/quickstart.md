# Quick Start Guide

## Setup
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Common Commands

### Testing
```bash
# Run all tests
make test

# Run module tests
make modules-test

# Run specific module tests
cd modules/Clinical && make test

# Run individual test file
python -m unittest modules/Clinical/tests/test_*.py -v
```

### Schema Generation
```bash
# Generate schema classes for all modules
make modules-gen

# Generate schema classes for specific module
cd modules/Clinical && make gen-schema
```

### Example Validation
```bash
# Validate examples
make test-examples
```

### CI Testing
```bash
# Using act (GitHub Actions local runner)
act -l  # List workflows
act pull_request  # Run PR workflow

# Manual CI testing
python -m venv ci-venv
source ci-venv/bin/activate
pip install -e .
make test
```

## Common Issues and Solutions

### Tests Failing
1. Check Python version (CI uses 3.10)
2. Verify dependencies: `pip install -e .`
3. Check environment variables

### Schema Issues
1. Regenerate schema: `make modules-gen`
2. Check YAML syntax
3. Verify required fields

### Import Errors
1. Check PYTHONPATH
2. Verify package installation
3. Check module structure

## Project Structure
```
htan-linkml/
├── modules/          # Module definitions
├── docs/            # Documentation
├── examples/        # Example data
├── src/            # Source code
└── Makefile        # Build rules
```

## Getting Help
- Check `docs/development.md` for detailed guide
- Review GitHub issues
- Contact maintainers 