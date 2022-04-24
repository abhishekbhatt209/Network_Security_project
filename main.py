import subprocess
from colorama import Fore, Back, Style
print(Fore.RED+ '''
NETWORK SECURITY PROJECT

====================================================
     $$$       $$       $$$$$$
    $$ $$     $$        $$
   $$   $$   $$         $$$$$$
  $$     $$ $$              $$
 $$       $$$           $$$$$$
====================================================


''')

print(Fore.GREEN +'''
Enter 1 for Network Sniffing
Enter 2 for Port Scaning
Enter 3 for Black-White-List IP Address

''')

c = int(input("Enter Your Choise:"))
if c == 1:
	cmd = "python3 newsniffer.py"
elif c == 2:
	cmd = "python3 IPScan.py"
elif c == 3:
	cmd = "python3 iptable.py"

else:
	print("Wrong input")
	
	
	
p = subprocess.Popen(cmd, shell=True)
out, err = p.communicate()
print(err)
print(out)
