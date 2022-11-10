@echo off
call conda activate
pip install -r requirements.txt
python run.py
pause