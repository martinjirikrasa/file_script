import os
import sys
import winreg as reg

cwd = os.getcwd()

exe_path = os.path.join(cwd, "tiskova_zakazka.exe")

key_path = r"Directory\Background\shell\Tiskova_zakazka"

key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, key_path)

reg.SetValue(key, '', reg.REG_SZ, '&Tisková zakázka')

key1 = reg.CreateKeyEx(key, r"command", 0, reg.KEY_SET_VALUE)

reg.SetValue(key1, '', reg.REG_SZ, r'"{}" "%V"'.format(exe_path))

###########################################################################
cwd = os.getcwd()

exe_path = os.path.join(cwd, "tisk1.exe")

key_path = r"Directory\\shell\\Tisk1"

key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, key_path)

reg.SetValue(key, '', reg.REG_SZ, '&Tisková zakázka')

key1 = reg.CreateKeyEx(key, r"command", 0, reg.KEY_SET_VALUE)

reg.SetValue(key1, '', reg.REG_SZ, r'"{}" "%V"'.format(exe_path))
