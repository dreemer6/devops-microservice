install:
	#install commands
	pip install --upgrade pip && \
		pip install -r requirements.txt
format:
	#format code
	black *.py mylib/*.py tests/*.py
lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib tests/test_*.py
build:
	#build container
deploy:
	#deploy
all: install lint test deploy