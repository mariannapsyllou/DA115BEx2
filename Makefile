# Variables
PYTHON=python3
COVERAGE=coverage

# Directories
SRC_DIR=src
TEST_DIR=$(SRC_DIR)/test

# Targets
test:
	$(PYTHON) -m unittest discover $(TEST_DIR)

coverage:
	$(COVERAGE) run --source=$(SRC_DIR) -m unittest discover $(TEST_DIR)
	$(COVERAGE) report -m

lint:
	pylint $(SRC_DIR)

flake8:
	flake8 $(SRC_DIR)

clean:
	$(COVERAGE) erase
