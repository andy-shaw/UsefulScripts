@echo off

echo Installing dictionary module to python 2.7 folder

xcopy C:\UsefulScripts\enable1.txt C:\Python27\Lib\ /Y /F
xcopy C:\UsefulScripts\dictionary.py C:\Python27\Lib\ /Y /F

xcopy C:\UsefulScripts\compress.py C:\Python27\Lib\ /Y /F

echo on