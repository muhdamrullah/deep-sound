import os
import subprocess
import time
from selenium import webdriver
from flask import Flask, redirect, render_template

def question():
    question_A = driver.find_element_by_xpath('//*[@id="bulle-inner"]')
    return driver.execute_script("return arguments[0].innerHTML", question_A)

def read_question():
    question_name = question()
    print question_name
    # Generates small talk
    small_talk = 'gtts-cli.py "%s" -l "en" -o question.mp3 && play question.mp3' % question_name
    subprocess.call(small_talk, shell=True)

def check_answer():
    print 'Initiating answer checking'
    if '#### insert url ####' in driver.current_url:
        persona = driver.find_element_by_id('perso')
        name_of_person = driver.execute_script("return arguments[0].innerHTML", persona)
        speech = 'I think of %s' % name_of_person
        answer_talk = 'gtts-cli.py "%s" -l "en" -o answer.mp3 && play answer.mp3' % speech
        subprocess.call(answer_talk, shell=True)
        print speech
        driver.quit()
        return 'True', name_of_person
    else:
        print driver.current_url
	return 'False', driver.current_url

driver = webdriver.PhantomJS(executable_path='./node_modules/phantomjs/lib/phantom/bin/phantomjs')

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
	global driver
        hitech = subprocess.Popen('exec play jeopardy.wav', shell=True)
	driver.quit()
	driver = webdriver.PhantomJS(executable_path='./node_modules/phantomjs/lib/phantom/bin/phantomjs')
	driver.set_window_size(1120, 550)
	driver.get("#### insert URL #####")
	driver.find_element_by_id('elokence_sitebundle_identification_age').send_keys("30")
	driver.find_element_by_xpath('//*[@id="infos-area-footer"]/input').click()
	print driver.current_url
	opening = 'Lets play a game. Think of someone in the world. I will ask a few questions. Just answer yes or no. Please hold for the first question'
	opening_talk = 'gtts-cli.py "%s" -l "en" -o opening.mp3 && play opening.mp3' % opening
	subprocess.call(opening_talk, shell=True)
	read_question()
        return render_template('./index.html')

@app.route("/no/", methods=['GET','POST'])
def no():
	driver.find_element_by_id('reponse2').click()
        time.sleep(3)
	valid, name_of_person = check_answer()
	if "True" in valid:
	    return name_of_person
	else:
	    pass
	read_question()
	return render_template('./index.html')

@app.route("/yes/", methods=['GET','POST'])
def yes():
	driver.find_element_by_id('reponse1').click()
        time.sleep(3)
	valid, name_of_person = check_answer()
        if "True" in valid:
            return name_of_person
        else:
            pass
	read_question()
        return render_template('./index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6006))
    app.run(host='0.0.0.0', port=port)
