@echo off
setlocal

:: Set Python version (change if needed)
python --version

call venv\Scripts\activate

:: Upgrade pip
python -m pip install --upgrade pip

:: Install dependencies
pip install -r requirements.txt

endlocal
