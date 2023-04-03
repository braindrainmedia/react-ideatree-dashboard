import os
import shutil

folder_a = '/Users/tre/Documents/Jeremi_Exp/GPT_Experiment/Folder'
folder_b = '/Users/tre/Documents/Jeremi_Exp/GPT_Experiment/Expanded_Results'

# Ensure that Folder B exists
if not os.path.exists(folder_b):
    os.makedirs(folder_b)

# Iterate through files in Folder A
for filename in os.listdir(folder_a):
    # Check if the file ends with 'EXP.txt'
    if filename.endswith('EXP.txt'):
        # Construct the source and destination file paths
        src = os.path.join(folder_a, filename)
        dest = os.path.join(folder_b, filename)
        
        # Move the file from Folder A to Folder B
        print("Moving file from {} to {}".format(src, dest))
        shutil.move(src, dest)
        print("Done moving file")
