import subprocess
from numpy import genfromtxt
import re
import time

process = subprocess.Popen('nmap -sP 192.168.1.1/24', shell=True, stdout=subprocess.PIPE)
output, err = process.communicate()
set1 = set(output.split())

while True:
    process_2 = subprocess.Popen('nmap -sP 192.168.1.1/24', shell=True, stdout=subprocess.PIPE)
    output_2, err_2 = process_2.communicate()
    print output_2

    # Check difference output
    set2 = set(output_2.split())
    difference_output = set2 - set1
    print set2 - set1

    # Read from known list of people
    my_listed_geo = genfromtxt('recorded-id.csv', delimiter=',', dtype=None)
    print my_listed_geo

    # Detect and speak for known list of people
    for user_id, name in enumerate(my_listed_geo):
        if (user_id, name)[1][0] in difference_output:
	   print (user_id, name)[1][1]
	   subprocess.Popen('play welcome.wav', shell=True)
	   time.sleep(4)
	   welcome_address = 'Welcome back %s, let me know if you need anything' % (user_id, name)[1][1]
	   command = 'gtts-cli.py "%s" -l "en" -o name.mp3 && play name.mp3' % welcome_address
           subprocess.call(command, shell=True)
        else:
	   pass
    set1 = set2
    time.sleep(5)
