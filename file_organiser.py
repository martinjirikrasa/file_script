import os
import shutil

os.mkdir("client")
os.mkdir("edit")
os.mkdir("checkout")

my_directory = os.getcwd()

original = r'C:\Users\marti\Desktop\test_matej_tst.txt'
new_name = "new_name.txt"
target = os.path.join(my_directory, "edit", new_name)

shutil.copyfile(original, target)