import subprocess
import time

def popen_timeout(command, timeout):
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    for t in xrange(timeout):
        time.sleep(1)
        if p.poll() is not None:
	    output, error = p.communicate()
	    if 'person:' in output:
		subprocess.Popen('play count.wav', shell=True)
		time.sleep(2)
		command_text = 'I detected %d person' % output.count('person')
		command = 'gtts-cli.py "%s" -l "en" -o human.mp3 && play human.mp3' % command_text
		subprocess.call(command, shell=True)
            return output
    p.kill()
    output, error = p.communicate()
    return output

while True:
    getFile = subprocess.call('wget -O boardroom.jpg http://192.168.1.164/picture/1/current', shell=True)
    changePNG = subprocess.call('mogrify -format png boardroom.jpg', shell=True)
    output =  popen_timeout(['./darknet','yolo', 'test', 'cfg/yolo.cfg', 'yolo.weights', './boardroom.png'], 30)
    print output
