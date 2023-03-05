<p align="left">
  Pig dice game with python OOP
  <br>
</p>


##  About

The project was created with Python OOP.
It consists of 8 classes which are game, intelligence, highscores,
dice_visual, menu, player, main and the shell which include the cmd commads.

One can play the game as single player versus Computer. For that purpose
class Intelligence was created and holds how the Computer will play the game
including 3 different levels of difficulty.
One can also play the game with another person.
One can see highscores and the instructions of the game at any time wishes as well
as restart the current game or switch between single and double player games.



## Instalation

Check version of Python

Check what version of Python you have. The Makefile uses `PYTHON=python3` as default.

```
# Check you Python installation
make version
```

If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.

```
# Set the environment variable to be your python executable
export PYTHON=python3
make version
```

### Python virtual environment

Install a Python virtual environment and activate it.

```
# Create the virtual environment
make venv

# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate
```

When you are done you can leave the venv using the command `deactivate`.

### Install the dependencies

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.

```
# Do install them
make install

# Check what is installed
make installed
```

### Run the code

The Pig game program can be started like this.

```
# First export the python to the directory with
export PYTHONPATH=.
# Then you can run the game with
python dice/main.py
```

All code is stored below the directory `dice/`.

##  Unittesting and validators

### Run the validators

You can run the static code validators like this. They check the sourcecode and exclude the testcode.

```
# Run each at a time
make flake8
make pylint

# Run all on the same time
make lint
```

You might need to update the Makefile if you change the name of the source directory currently named `dice/`.

### Run the unittests

You can run the unittests like this. The testfiles are stored in the `test/` directory.

```
# Run unttests without coverage
make unittest

# Run unittests with coverage
make coverage

# Run the linters and the unittests with coverage
make test
```

You can open a web browser to inspect the code coverage as a generated HTML report.



## Remove generated files

You can remove all generated files by this.

```
# Remove files generated for tests or caching
make clean

# Do also remove all you have installed
make clean-all
```

## Create a fresh copy of the documentation

You can create a fresh copy of the docs by this.

```
# Create new copy in HTML version
make doc

#Create new copy of UML diagrams
make uml
```

## Authors
 Axel Friberg
 Marianna Psyllou
