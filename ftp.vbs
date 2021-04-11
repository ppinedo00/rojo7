'PRUEBA FTP
'AGS

dim oexec, cmd
cmd="mkdir C:\EXCEL\pepeVBS"
set WshShell = CreateObject("WScript.Shell")
set oExec = WshShell.exec("cmd.exe /c" & cmd)

