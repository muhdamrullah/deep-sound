# **Code Example** 
Code Example

For the sake of brevity, you should download all the libraries necessary before executing the script 
```
$ sudo apt-get update && sudo apt-get install sox libsox-fmt-all

$ sudo pip install gTTS
```
Insert the keys for the 'Google' service

```
$ nano listen_to_my_request.py
```
A. Ensure that your microphone is plugged in and run the Python Flask

```
$ python app.py
```
B. To retrieve abnormal detection, run alert.py in another terminal

```
$ python alert.py
```
C. To retrieve welcome detection, run geolocation.py in another terminal

```
$ python geolocation.py
```
D. To retrieve news alerts, run bbc_news.py in another terminal

```
$ python bbc_news.py
```
E. To retrieve body count, run /darknet/darknet.py in another terminal

```
$ cd darknet
$ python darknet.py
```
