import subprocess
import time

while True:
    insert_H_client_id = '<insert_client_id>'
    insert_H_client_key = '<insert_key_here>'
    command_to_play_audio = 'rec -p | sox - -c 1 -r 16000 -t s16 -L - | python sample_stdin.py %s %s' % (insert_H_client_id, insert_H_client_key)
    process = subprocess.Popen(command_to_play_audio, shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()    
    print(out)
    time.sleep(2)
    if "mom" in out:
	print "Successful"
        break
