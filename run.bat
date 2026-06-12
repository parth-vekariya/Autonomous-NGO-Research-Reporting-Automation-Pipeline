@echo off
echo ============================================
echo   NGO Research Automation Pipeline
echo ============================================
pip install -r requirements.txt -q
python src/main.py
echo.
echo Files ready in the output\ folder.
pause
