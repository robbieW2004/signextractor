def extract():
    import subprocess
    with open("output.txt") as f:
        lines = f.readlines()
        y = len(lines)
        x = 0
    while x < y:
        filename = lines[x].rstrip()
        print(x, filename)
        program='NBTUtil.exe'
        arguments=f'--path=C:\\Users\\...\\signextractor\\regions\\{filename}' # put the path where you have the region files like this C:\\Users\\*username*\\...... double dash is important
        argument2='--printtree'
        argument3=f'> C:\\Users\\...\\signextractor\\{filename}.txt' # put the path to the folder this program is in 
        print(program, arguments, argument2, argument3)
        with open(f'C:\\Users\\...\\signextractor\\{filename}.txt', "w") as outfile: # put the same path here that you did at line 14
            subprocess.call([program, arguments, argument2], stdout=outfile)
        x = x+1
extract()
