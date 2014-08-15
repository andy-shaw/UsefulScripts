@echo off

set place=%1

if "%place%"=="py" goto :py
if "%place%"=="java" goto :java

goto :error

:py
echo Going to Python Challenges
cd "C:\Users\%USERNAME%\Documents\Programming\Python\Daily Challenges"
goto :end

:java
echo Going to Java Challenges
cd "C:\Users\%USERNAME%\Documents\Programming\Java\Daily Challenges"
goto :end

:error
echo "USAGE: challenge [py|java]"

:end
echo on