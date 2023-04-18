@echo off
if not defined minimized set minimized=1 && start /min run.bat && exit
set python="python-3.9.13-embed-amd64/python.exe"
%python% run.py
exit
