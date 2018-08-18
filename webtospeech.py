from bs4 import BeautifulSoup
import urllib
import re
from gtts import gTTS
from pygame import mixer

mixer.init()
print("Enter the Url")
url = input()
print("\n\n")
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
	print(t)
	tts = gTTS(text= t, lang='en')
	tts.save("tmp.mp3")
	mixer.music.load("tmp.mp3")
	mixer.music.play()
	while mixer.music.get_busy():
		pass
	
