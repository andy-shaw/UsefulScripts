@echo off
echo Running aliases

echo ----subl = sublime text
echo ----n++ = notepad++
echo ----winscp = winscp

doskey subl="C:\Program Files\Sublime Text 2\sublime_text.exe" $*
doskey n++="C:\Program Files (x86)\Notepad++\notepad++.exe" $*
doskey winscp="C:\Program Files (x86)\WinSCP\WinSCP.exe" $*



echo on