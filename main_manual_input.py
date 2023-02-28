import subprocess
import config


DROP_FOLDER = config.DROP_FOLDER
POWERSHELL_PATH = "%SystemRoot%\system32\WindowsPowerShell\\v1.0\powershell.exe"

print("End program with ctrl + c")

while True:
    user_input_name = input("Name of shortcut: ")
    user_input_ip = input("IP/hostname: ")

    #SHORTCUT NAME ALL IN UPPER (DELETE upper() IF YOU DON'T WANT CAPITALS)
    shortcut_path = DROP_FOLDER + user_input_name + ".url"
    #CREATE URL + ADD DOMAIN NAME
    shortcut_url = "http://" + user_input_ip + "/"


    #POWERSHELL COMMANDS:
    l = ["$WshShell = New-Object -comObject WScript.Shell", 
        "$Shortcut = $WshShell.CreateShortcut('%s')"%shortcut_path, 
        "$Shortcut.TargetPath = '%s'"%shortcut_url,
        "$Shortcut.Save()"]
    

    #FULL COMMAND SAVED
    end_command = POWERSHELL_PATH + ' ' + "%s"%l[0] + ";" + "%s"%l[1] + ";" + "%s"%l[2] + ";" + "%s"%l[3]

    #RUN POWERCHELL COMMAND
    subprocess.call(end_command, shell=True)