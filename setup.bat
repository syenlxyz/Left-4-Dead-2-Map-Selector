@echo off
call conda activate
pip install pipreqs --ignore-installed
pipreqs --force --mode no-pin
pip install --requirement requirements.txt --ignore-installed
pause