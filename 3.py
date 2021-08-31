import os
for root, dirs, files in os.walk("."):
    for filename in files:
        if ".mca.txt" in filename:
            N = 4
            with open(filename, 'r') as f:
                lines = f.read().splitlines()
                for i, line in enumerate(lines):
                    if "id: minecraft:sign" in line:
                        j = i-N if i>N else 0
                        for k in range(j,i + 5):
                            print(lines[k])