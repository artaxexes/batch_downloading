Option Explicit

Const ForReading = 1
Dim oFSO: Set oFSO = CreateObject("Scripting.FileSystemObject")
Dim oFile: Set oFile = oFSO.OpenTextFile("id.txt", ForReading)

Do While oFile.AtEndOfStream = False

	Dim fileName: fileName = oFile.ReadLine & ".jpg"
	Dim oXMLHTTP: Set oXMLHTTP = CreateObject("MSXML2.XMLHTTP.3.0")
	oXMLHTTP.open "GET", "http://www.camara.leg.br/internet/deputado/bandep/" & fileName, False
	oXMLHTTP.send
	If oXMLHTTP.status = 200 Then
		
	End If
	Set oXMLHTTP = Nothing
	
Loop