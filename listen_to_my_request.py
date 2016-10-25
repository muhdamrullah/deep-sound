import subprocess
import time

while True:
    # Generates small talk
    small_talk = 'gtts-cli.py "%s" -l "en" -o hello.mp3 && play hello.mp3' % 'Hello.'
    subprocess.call(small_talk, shell=True)
    time.sleep(2)
    insert_H_client_id = '<insert_client_id>'
    insert_H_client_key = '<insert_client_key>'
    command_to_play_audio = 'rec -p | sox - -c 1 -r 16000 -t s16 -L - | python sample_stdin.py %s %s' % (insert_H_client_id, insert_H_client_key)
    process = subprocess.Popen(command_to_play_audio, shell=True, stdout=subprocess.PIPE)
    output, err = process.communicate()    
    print(output)
    time.sleep(2)
    if "hey" in output:
	subprocess.call('python read_body.py', shell=True)
	print "Successful"
        break
