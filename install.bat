@echo off
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
start /wait "" Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /AddToPath=1 /RegisterPython=1 /S /D=%UserProfile%\Miniconda3
pause