import sys
import os
import shutil

if len(sys.argv) > 1:
    selected_folder = sys.argv[1]
else:
    print("No folder path provided")
    exit()

client_dir = os.path.join(selected_folder, "client")
edit_dir = os.path.join(selected_folder, "edit")
checkout_dir = os.path.join(selected_folder, "checkout")
os.makedirs(client_dir, exist_ok=True)
os.makedirs(edit_dir, exist_ok=True)
os.makedirs(checkout_dir, exist_ok=True)

my_directory = os.getcwd()
original = r'\\Nas-inet-data\inet-data\iB2BC-DTP\Makety\Vzor\iNETPrintCZ - Template.ai'
new_name = f"iNETPrintCZ - {os.path.basename(selected_folder)}.ai"
target = os.path.join(edit_dir, new_name)
shutil.copyfile(original, target)
