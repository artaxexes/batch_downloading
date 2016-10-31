Option Explicit

Const ForReading = 1
Dim oFSO: Set oFSO = CreateObject("Scripting.FileSystemObject")
Dim oFile: Set oFile = oFSO.OpenTextFile("id.txt", ForReading)

Do While oFile.AtEndOfStream = False

	MsgBox oFile.ReadLine
	
Loop