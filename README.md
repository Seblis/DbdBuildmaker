# DbdBuildmaker
Web app allowing to create and manage perk builds for the game Dead by Daylight - currently on a very slow development as I am occupied by other personal projects

## Virtual environment setup
Right now project is running on Django 4.1.2 with Python 3.10. If you have Python 3.10 installed, you can simply call `python -m venv .venv` in Powershell. After that, activate virtual environment and install Django and other dependencies with

```
./.venv/Scripts/Activate.ps1
pip install -r requirements.txt
```

and you're good to go.

Later on you will use all Django commands after enabling virtual environment with the script `Activate.ps1` like the first line above.

## Code formatting

The code will be eventually formatted with Black formatter (https://github.com/psf/black) with string normalization disabled. In case you are using a VS Code, install "Black Formatter" extension and then find **Extensions > Black Formatter > Manage > Extension settings** on the following screen, find `Black-formatter:Args`, click "Add item" and add item `--skip-string-normalization`
