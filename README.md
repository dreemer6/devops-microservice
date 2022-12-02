
# Python Microservice DevOps Demo

## Steps

### Create a virtual environment

`python3 -m venv ~/.venv` or `virtualenv ~/.venv`

### Source the environment in the ~/.bashrc file

`nano ~/.bashrc` -> On the last line of the file enter `source ~/.venv/bin/activate` then save file.
Now every new Terminal window will open with the .venv environment

### Create empty files

`touch requirements.txt Dockerfile Makefile main.py`
`mkdir mylib`
`cd mylib`
`touch __init__.py logic.py`
`cd ..`

### Populate Makefile
