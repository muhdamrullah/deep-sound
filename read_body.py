import urllib2
import subprocess
import random

# Generates small talk

lines = open('random_talk.csv').read().splitlines()
myline = random.choice(lines)
small_talk = 'gtts-cli.py "%s" -l "en" -o hello.mp3 && play hello.mp3' % myline
subprocess.call(small_talk, shell=True)

# Open the localhost to get data
response = urllib2.urlopen('http://192.168.1.145:6006/')
html = response.read()
print html

# Initializing analysis
command = 'gtts-cli.py "%s" -l "en" -o hello.mp3 && play hello.mp3' % html
subprocess.call(command, shell=True)
