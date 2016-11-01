Option Explicit

Const ForReading = 1
Const TristateTrue = 1

Dim fso: Set fso = CreateObject("Scripting.FileSystemObject")
Dim txtFile: Set txtFile = fso.OpenTextFile("info2.txt", ForReading, TristateTrue)

Do While txtFile.AtEndOfStream = False

	Dim id: id = txtFile.ReadLine
	Dim xmlHttp : Set xmlHttp = CreateObject("MSXML2.XMLHTTP.3.0")
	xmlHttp.open "GET", "http://www.camara.leg.br/internet/deputado/bandep/" & id, False
	xmlHttp.send
	If xmlHttp.status = 200 Then
		Dim stream: Set stream = CreateObject("ADODB.Stream")
		stream.Open
		stream.Type = 1
		stream.Write xmlHttp.responseBody
		stream.SaveToFile "img\" & id
		stream.Close
		Set stream = Nothing
	End If
	Set xmlHttp = Nothing
	
Loop