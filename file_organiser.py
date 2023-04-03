import os
import shutil

os.mkdir("client")
os.mkdir("edit")
os.mkdir("checkout")

my_directory = os.getcwd()

# original - path to the file we want to copy
original = r'C:\Users\marti\Desktop\test_matej_tst.txt'
cesta = my_directory.split("\\")
last = cesta[-1]
new_name = f"{last}.txt"

target = os.path.join(my_directory, "edit", new_name)

shutil.copyfile(original, target)
