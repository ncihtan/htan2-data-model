# Development Guide

This guide covers development workflows, testing procedures, and CI/CD processes for the HTAN LinkML project.

## Table of Contents
- [Local Development Setup](#local-development-setup)
- [Testing Locally](#testing-locally)
- [Testing CI Workflows Locally](#testing-ci-workflows-locally)
- [Project Structure](#project-structure)
- [Common Development Tasks](#common-development-tasks)

## Local Development Setup

### Prerequisites
- Python 3.10 or higher
- Git
- Poetry (Python package manager)

### Initial Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd htan-linkml
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

## Testing Locally

### Running All Tests
```bash
make test
```
This command runs:
- All module tests
- Example validation tests
- Schema validation tests

### Running Specific Module Tests
```bash
make modules-test
```
This runs tests for all modules defined in the Makefile.

### Running Tests for a Specific Module
```bash
cd modules/Clinical
make test
```

### Running Individual Test Files
```bash
python -m unittest modules/Clinical/tests/test_*.py -v
```

### Running Example Validation
```bash
make test-examples
```
This validates all example files against the schema.

## Testing CI Workflows Locally

### Using act (GitHub Actions Local Runner)
1. Install act:
   ```bash
   brew install act  # macOS
   # or
   choco install act-cli  # Windows
   ```

2. Run the CI workflow locally:
   ```bash
   act -l  # List available workflows
   act pull_request  # Run the pull request workflow
   ```

### Manual CI Testing
To simulate CI environment locally:

1. Create a clean environment:
   ```bash
   python -m venv ci-venv
   source ci-venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   ```

3. Run tests:
   ```bash
   make test
   ```

## Project Structure

```
htan-linkml/
├── modules/
│   └── Clinical/
│       ├── domains/        # Schema definitions
│       ├── src/           # Generated code
│       ├── tests/         # Test files
│       └── Makefile       # Module-specific build rules
├── docs/                  # Documentation
├── examples/             # Example data
├── src/                  # Source code
└── Makefile             # Global build rules
```

## Common Development Tasks

### Adding a New Module
1. Create module directory in `modules/`
2. Add module name to `MODULES` in root Makefile
3. Create module-specific Makefile
4. Add tests and documentation

### Updating Schema
1. Modify schema files in `modules/Clinical/domains/`
2. Regenerate schema classes:
   ```bash
   make modules-gen
   ```
3. Update tests if needed
4. Run tests to verify changes

### Adding New Tests
1. Create test file in `modules/Clinical/tests/`
2. Follow existing test patterns
3. Add test data files if needed
4. Run tests to verify

### Documentation Updates
1. Update relevant markdown files in `docs/`
2. Verify formatting
3. Commit changes

## Troubleshooting

### Common Issues

1. **Tests failing locally but passing in CI**
   - Check Python version matches CI (3.10)
   - Verify all dependencies are installed
   - Check environment variables

2. **Schema generation issues**
   - Verify YAML syntax
   - Check for circular dependencies
   - Ensure all required fields are defined

3. **Import errors**
   - Check PYTHONPATH
   - Verify package installation
   - Check module structure

### Getting Help
- Check existing issues on GitHub
- Review documentation
- Contact maintainers

## Best Practices

1. **Code Style**
   - Follow PEP 8
   - Use type hints
   - Document complex functions

2. **Testing**
   - Write tests for new features
   - Include both positive and negative test cases
   - Keep tests focused and independent

3. **Documentation**
   - Update docs with new features
   - Include examples
   - Keep README current

4. **Version Control**
   - Use meaningful commit messages
   - Follow conventional commits
   - Keep commits focused 