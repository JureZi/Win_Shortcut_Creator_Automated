# Win_Shortcut_Creator_Automated
Python script to create multiple shortcuts in Windows via PowerShell.


I had a problem in at job. i needed shortcuts for around 30 printers, so I created script for automation.
Printers have almost the some hostname except for the end number. One script is also made for manual inputs.


Just put your path in config.py and you should be good! :)




POWERSHELL COMMAND used in scripts:

$WshShell = New-Object -comObject WScript.Shell $Shortcut = $WshShell.CreateShortcut("$Home\Desktop\DROP_FOLDER\t-di-vit-001.lnk") $Shortcut.TargetPath = "http://t-di-vit-001.some-domain.com/" $Shortcut.Save()
