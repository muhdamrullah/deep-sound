from flask import Flask
import subprocess
import os
import random
import time

def trigger_message(user_id):
    subprocess.Popen('play transformers.wav fade h 0 0 5', shell=True)
    # Choose random welcome speech
    time.sleep(4)
    welcome_talk = open('welcome_talk_v2.csv').read().splitlines()
    welcome_line = random.choice(welcome_talk)
    welcome_address = 'Authenticating %s.' % user_id
    command = 'gtts-cli.py "%s" -l "en" -o facename.mp3 && play facename.mp3' % welcome_address
    subprocess.call(command, shell=True)
    time.sleep(5)
    welcome_address_2 = '%s' % welcome_line
    command_2 = 'gtts-cli.py "%s" -l "en" -o auth.mp3 && play auth.mp3' % welcome_address_2
    subprocess.call(command_2, shell=True)
#    wemo_status = subprocess.output('wemo -v switch "Facerecog Asia" status', shell=True)
    p = subprocess.Popen('wemo -v switch "Facerecog Asia" status', shell=True, stdout=subprocess.PIPE)
    wemo_status, err = p.communicate()
    if 'off' in wemo_status:
	subprocess.call('wemo switch "Facerecog Asia" on', shell=True)
    else:
	subprocess.call('wemo switch "Facerecog Asia" off', shell=True)    

welcome_talk = open('welcome_talk_v2.csv').read().splitlines()

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello():
    subprocess.call('play intro_to_space.wav fade h 0 0 5', shell=True)
    return 'Hello'

@app.route('/user/<person_id>', methods=['GET','POST'])
def user(person_id):
    if 'low' in person_id:
	pass
    elif '0' in person_id:
	trigger_message('Amrullah')
    elif '1' in person_id:
	trigger_message('Eugene')
    else:
	pass
    return person_id
   
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6005))
    app.run(host='0.0.0.0', port=port)
