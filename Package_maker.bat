@echo off
set cuurent_dir=%~dp0

SET PYTHONPATH=%PYTHONPATH%;%cuurent_dir%venv\Lib\site-packages

echo Current location: %cuurent_dir%

%cuurent_dir%venv\Scripts\python.exe %cuurent_dir%main.py

pause