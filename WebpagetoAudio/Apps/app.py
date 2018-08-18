from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import urllib
from gtts import gTTS
import pygame
import os


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def get_audio():
	url = request.form["url_box"]
	
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}

	req = urllib.request.Request(url, headers=hdr)

	page_html = urllib.request.urlopen(req).read()
	soup = BeautifulSoup(page_html, 'html.parser')

	text = soup.findAll('p')

	for t in text:
		t = t.text
		tts = gTTS(text= t, lang='en')
		tts.save("tmp/tmp.mp3")
		pygame.mixer.init()
		pygame.mixer.music.load("tmp/tmp.mp3")
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy():
			pass
		pygame.mixer.quit()
		
	
	return render_template('index.html')

if __name__ == "__main__":

    app.debug = True
    app.run()
    printtext()