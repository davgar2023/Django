# Contributing to Django Repository

Thank you for your interest in contributing to this Django repository! Here are the guidelines to help you get started.

## Code of Conduct

- Be respectful and professional in all interactions
- Provide constructive feedback
- Help create an inclusive and welcoming environment

## How to Contribute

### Reporting Bugs

1. **Check if the bug has already been reported** by searching [existing issues](https://github.com/davgar2023/Django/issues)
2. **Create a new issue** with a clear title and description
3. **Include relevant details**:
   - Python version
   - Django version
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Error messages or logs

### Suggesting Enhancements

1. **Use a clear, descriptive title**
2. **Provide a step-by-step description** of the suggested enhancement
3. **Provide specific examples** to demonstrate the steps
4. **Explain why this enhancement would be useful**

### Pull Requests

1. **Fork the repository** and create your feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following Django best practices

3. **Write or update tests** to cover your changes

4. **Ensure code quality**:
   ```bash
   python manage.py test
   ```

5. **Commit your changes** with clear, descriptive messages:
   ```bash
   git commit -m "Add feature: description of what was added"
   ```

6. **Push to your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request** with a clear description of changes

## Development Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install pytest pytest-django
   ```

3. Create a `.env` file from `.env.example`:
   ```bash
   cp .env.example .env
   ```

4. Run tests:
   ```bash
   python manage.py test
   ```

## Coding Standards

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Write tests for new features

## Commit Message Guidelines

- Use the imperative mood ("add feature" not "added feature")
- Limit the first line to 72 characters or less
- Reference relevant issues and pull requests liberally after the first line

Example:
```
Add user authentication API endpoint

- Implement JWT token generation
- Add user login validation
- Update API documentation

Fixes #123
```

## Questions?

Feel free to open an issue with the "question" label or reach out to the maintainers.

Thank you for contributing!
