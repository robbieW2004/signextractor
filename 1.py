import os
for root, dirs, files in os.walk("."):
    for filename in files:
        if ".mca" in filename:
            print(filename)