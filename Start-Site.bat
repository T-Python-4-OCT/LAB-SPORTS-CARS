@echo off
cd /d "%~dp0"
echo Starting the Sports Cars site...
echo Open http://127.0.0.1:8000/ in your browser.
echo Keep this window open while using the site.
echo.
"%~dp0.venv\Scripts\python.exe" manage.py runserver 127.0.0.1:8000
echo.
echo The server has stopped.
pause
