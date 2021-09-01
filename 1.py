import sys
import os
def listmcas():
    original_stdout = sys.stdout
    for root, dirs, files in os.walk("."):
        for filenames in files:
            if ".mca" in filenames:
                print(filenames)
                with open('output.txt', 'w') as outfile:
                    sys.stdout = outfile
                    for filenames in files:
                        print(filenames)
                    sys.stdout = original_stdout
listmcas()