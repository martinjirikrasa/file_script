import os
import sys
import winreg as reg

cwd = os.getcwd()

python_exe = sys.executable

key_path = r"Directory\\Background\\shell\\Tiskova_zakazka"

key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, key_path)

reg.SetValue(key, '', reg.REG_SZ, '&Tisková zakázka')

key1 = reg.CreateKeyEx(key, r"command", 0, reg.KEY_SET_VALUE)

reg.SetValue(key1, '', reg.REG_SZ, r'{} "{}\file_organiser.py" "%V"'.format(python_exe, cwd))
