install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv calc_test.py

format:
	black *.py 



lint:
	pylint --disable=R,C calc.py

all: install lint test