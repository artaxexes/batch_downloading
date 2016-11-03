Option Explicit

Dim wShell: Set wShell = CreateObject("WScript.Shell")
wShell.Run "C:\Strawberry\perl\bin\perl.exe down-this-from.pl", 0, False
Set wShell = Nothing