import subprocess

print_output = ""

for ping in range(1,10): 
    address = "192.168.1." + str(ping)

    #NEXT LINE MAY DIFFER DUE TO OS:
    output = subprocess.Popen(["ping.exe",address],stdout = subprocess.PIPE).communicate()[0]

    if str(output).find("unreachable") == -1:
        print_output += "{} is online\n".format(address)
    else:
        print_output += "{} is offline\n".format(address)

print(print_output)