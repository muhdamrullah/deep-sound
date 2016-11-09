import subprocess
from numpy import genfromtxt
import re
import time
import random

# Parameters

time_limit = 600

process = subprocess.Popen('nmap -sP 192.168.1.1/24', shell=True, stdout=subprocess.PIPE)
output, err = process.communicate()
set1 = set(output.split())

blacklist = []

def trigger_message(user_id):
    subprocess.Popen('play welcome.wav', shell=True)
    time.sleep(4)
    # Choose random welcome speech
    welcome_talk = open('welcome_talk.csv').read().splitlines()
    welcome_line = random.choice(welcome_talk)
    welcome_address = 'Welcome back %s, %s' % ((user_id, name)[1][1], welcome_line)
    command = 'gtts-cli.py "%s" -l "en" -o name.mp3 && play name.mp3' % welcome_address
    subprocess.call(command, shell=True)

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
	   triggered_name = (user_id, name)[1][1]
	   print 'Registered %s for the first time' % triggered_name
	   if triggered_name in str(blacklist):
		for array_id, black_id in enumerate(blacklist):
                    if black_id[0] == triggered_name and abs(time.time() - black_id[1]) > time_limit:
                        trigger_message(user_id)
                        black_id[1] = time.time()
                        print black_id[1]
                        print 'Youre above the time limit'
                    elif black_id[0] == triggered_name:
                        print 'Youre still within time limit'
			black_id[1] = time.time()
		    else:
			pass
			
	   else:
		print 'First append'
 	        trigger_message(user_id)
	        blacklist.append([triggered_name, time.time()])
        else:
	   pass
    set1 = set2
    time.sleep(5)
