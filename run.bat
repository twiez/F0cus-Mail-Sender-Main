@echo off
cd /d %~dp0

title Checking Python installation...
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed! (Go to https://www.python.org/downloads and install the latest version.^)
    echo Make sure it is added to PATH.
    goto ERROR
)

title Checking libraries...
echo Checking 'tkinter' (1/4)
python -c "import tkinter as tk" > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing tkinter...
    python -m pip install tkinter > nul
)

echo Checking 'smtplib' (2/4)
python -c "import smtplib" > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing smtplib...
    python -m pip install smtplib > nul
)


cls
title Starting builder...
python main.py
if %errorlevel% neq 0 goto ERROR
exit

:ERROR
color 4 && title [Error]
pause > nul
