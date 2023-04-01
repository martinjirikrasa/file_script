# file_script

This code is used to create a registry entry in the Windows Registry that will add a new option in the right-click context menu for files and directories. The added option will be called "&Tisková zakázka" and will execute the "file_organizer.py" script when clicked.

The first step is to import the required modules, namely os, sys, and winreg. Then, the current working directory (cwd) and the path to the Python executable (python_exe) are retrieved using the respective functions.

Next, a registry key is created under HKEY_CLASSES_ROOT, which is the root of the Windows Registry. The key's path is "Directory\Background\shell\Tiskova_zakazka", and it represents the new option that will be added to the right-click context menu.

After creating the key, its default value is set to "&Tisková zakázka" using the SetValue() function. This value represents the text that will be displayed in the context menu.

Then, a subkey called "command" is created under the main key. This subkey is where the command that will be executed when the option is clicked will be stored. The subkey's path is "Directory\Background\shell\Tiskova_zakazka\command".

Finally, the command to execute is set as the default value of the "command" subkey using the SetValue() function. The command consists of the Python executable path, the path to the "file_organizer.py" script, and the "%V" placeholder, which represents the path of the selected file or directory.

Overall, this code can be used to add a new option to the right-click context menu, making it easy to execute the "file_organizer.py" script on selected files and directories.
