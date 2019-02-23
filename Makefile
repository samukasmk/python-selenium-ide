SHELL=/bin/bash
.DEFAULT_GOAL=none

SUDO=sudo

help:
	@echo 'Makefile for Jenkins CI                                                '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '    make clean           Clean cache files for tests and future builds '
	@echo '    make test            Run tests with pytest                         '
	@echo '    make coverage        Run tests with pytest and coverage on terminal'
	@echo '    make coverage-html   Run tests with pytest and coverage on HTML    '
	@echo '    make coverage-xml    Run tests with pytest and coverage on xmls    '

### Clean (targets)
clean:
	$(SUDO) rm -fr htmlcov;
	$(SUDO) rm -fr .cache;
	$(SUDO) rm -fr .coverage;
	$(SUDO) rm -fr .pytest_cache;
	$(SUDO) rm -fr junit.xml coverage.xml;
	$(SUDO) find . -iname '*.pyc' -delete;
	$(SUDO) find . -iname '*.pyo' -delete;
	$(SUDO) find . -name '*,cover' -delete;
	$(SUDO) find . -iname __pycache__ -delete;


### Py.Test (targets)
test:
	pytest

coverage: clean
	pytest --cov=. --cov-report term

coverage-html: clean
	pytest --cov=. --cov-report html

coverage-xml: clean
	pytest --cov=. --cov-report xml:coverage.xml --junit-xml=junit.xml

