
# Python Microservice DevOps Demo

[![Python application test with Github Actions](https://github.com/dreemer6/devops-microservice/actions/workflows/devops.yml/badge.svg)](https://github.com/dreemer6/devops-microservice/actions/workflows/devops.yml)


## Steps

1. Create a virtual environment
`python3 -m venv ~/.venv` or `virtualenv ~/.venv`

2. Source the environment in the ~/.bashrc file
`nano ~/.bashrc` -> On the last line of the file enter `source ~/.venv/bin/activate` then save file.
Now every new Terminal window will open with the .venv environment

3. Create empty files
`touch requirements.txt Dockerfile Makefile main.py`
`mkdir mylib`
`cd mylib`
`touch __init__.py logic.py`
`cd ..`

4. Populate `Makefile`

5. Setup Continuous Integration and check for code issues
