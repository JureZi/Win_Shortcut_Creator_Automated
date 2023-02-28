import subprocess
import config

"""
I need to have shortcuts for 14 printers accessing link:
t-di-tk-001.some-domain.com
t-di-tk-002.some-domain.com
t-di-tk-003.some-domain.com
...
"""



DROP_FOLDER = config.DROP_FOLDER

POWERSHELL_PATH = "%SystemRoot%\system32\WindowsPowerShell\\v1.0\powershell.exe"


two_decimals = False
three_decimals = False


class Command_processing:
    def processing(user_input, printer_number, two_decimals, three_decimals):
        #CHECKING IF USER INPUT FULL HOSTNAME WITH PRITNER NUMBER - t-di-tk-001 INSTEAD OF t-di-tk
        if "0" in user_input:
            #t-di-tk-001 REPLACED WITH t-di-tk
            user_input = user_input.split("-0")[0]


        #CHEKING THE NUMBER OF DECIMALS SO THE PROGRAM KNOWS WHEN TO MOVE FROM 001 - 010 -100
        if printer_number % 10 == 0:
            two_decimals = True
        if printer_number % 100 == 0:
            three_decimals = True
        if not two_decimals and not three_decimals:
            shortcut_name = user_input + "-" + "00" + str(printer_number)
        if two_decimals and not three_decimals:
            shortcut_name = user_input + "-" + "0" + str(printer_number)
        if three_decimals and two_decimals:
            shortcut_name = user_input + "-" + str(printer_number)


        #SHORTCUT NAME ALL IN UPPER (DELETE upper() IF YOU DON'T WANT CAPITALS)
        shortcut_path = DROP_FOLDER + shortcut_name.upper() + ".url"


        #CREATE URL + ADD DOMAIN NAME
        shortcut_url = "http://" + shortcut_name + ".some-domain.com" + "/"

        #LIST WITH POWERSHELL COMMANDS
        l = ["$WshShell = New-Object -comObject WScript.Shell", 
            "$Shortcut = $WshShell.CreateShortcut('%s')"%shortcut_path, 
            "$Shortcut.TargetPath = '%s'"%shortcut_url,
            "$Shortcut.Save()"]
        
        #FULL COMMAND SAVED
        final_command = POWERSHELL_PATH + ' ' + "%s"%l[0] + ";" + "%s"%l[1] + ";" + "%s"%l[2] + ";" + "%s"%l[3]
        return final_command, two_decimals, three_decimals



print("End program with ctrl + c")
user_input = input("Name of printer: ")
printers_number = int(input("Number_of_printers: "))
loop = 0


while printers_number > loop:
    printer_number = loop + 1
    final_command, two_decimals, three_decimals = Command_processing.processing(user_input, printer_number, two_decimals, three_decimals)
    #RUN POWERCHELL COMMAND
    subprocess.call(final_command, shell=True)
    loop+=1