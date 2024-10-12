# Define the main script
MAIN_SCRIPT = ./ui/main.py

# Define the Python interpreter
PYTHON = python3

# Define the test command
TEST_CMD = pytest

# Define the requirements file
REQUIREMENTS = requirements.txt

# Start the application
start:
	$(PYTHON) $(MAIN_SCRIPT)

# Run tests
test:
	$(TEST_CMD)

# Clean temporary files and build artifacts
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

# Install dependencies
install:
	pip install -r $(REQUIREMENTS)