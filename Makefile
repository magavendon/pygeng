# Makefile for the python package using pipenv.

PACKAGE_NAME != sed -n "s/\s*name='\(.*\)'.*/\1/p" ./setup.py
PACKAGE_DIR := $(notdir $(CURDIR))
WORKON_HOME ?= $(HOME)/.virtualenvs
VIRTUAL_ENV != find $(WORKON_HOME) -type d -name "$(PACKAGE_DIR)*"
PYTHON=${VIRTUAL_ENV}/bin/python
MAKE := $(MAKE) --no-print-directory

default:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo
	@echo 'Usage:'
	@echo
	@echo '    make install    install the package in a virtual environment'
	@echo '    make activate   activate the virtual environment'
	@echo '    make dev        install the dev package in a virtual environment'
	@echo '    make reset      recreate the virtual environment'
	@echo '    make remove     remove the virtual environment'
	@echo '    make clean      cleanup all temporary files'
	@echo


venv: $(VIRTUAL_ENV)/bin/activate
$(VIRTUAL_ENV)/bin/activate: setup.py
	test -d "$(VIRTUAL_ENV)" || pipenv install

install: venv
	pipenv run which $(PACKAGE_NAME)

activate: install
	pipenv shell

dev: venv
	pipenv install --dev
	pipenv run which $(PACKAGE_NAME)

reset:
	$(MAKE) remove
	$(MAKE) install

remove:
	$(MAKE) clean
	pipenv --rm

clean:
	@rm -Rf *.egg .cache .coverage .tox build dist docs/build htmlcov
	@find -depth -type d -name __pycache__ -exec rm -Rf {} \;
	@find -depth -type d -name "*.egg-info" -exec rm -Rf {} \;
	@find -type f -name '*.pyc' -delete

.PHONY: default install reset clean test



