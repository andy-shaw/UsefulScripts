@echo off

echo Installing dictionary module to python 2.7 folder

xcopy enable1.txt C:\Python27\Lib\ /Y /F
xcopy dictionary.py C:\Python27\Lib\ /Y /F

echo on