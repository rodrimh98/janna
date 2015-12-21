import pyaudio
import wave
import sys
import os

import pyttsx

def record():
	#recording vars
	chunk = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 16000
	RECORD_SECONDS = 2
	WAVE_OUTPUT_FILENAME = "record.wav"
	all = []

	p = pyaudio.PyAudio()
	#stream process start
	stream = p.open(format = FORMAT,
					channels = CHANNELS,
					rate = RATE,
					input = True,
					frames_per_buffer = chunk)
	print "=> Recording"
	for i in range(0, RATE / chunk * RECORD_SECONDS):
		data = stream.read(chunk)
		all.append(data)
	print "=> Recording finished"
	stream.close()
	p.terminate()

	#writing to a file
	data = ''.join(all)

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwdth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(data)
	wf.close

	os.system('flac -f --best --sample-rate 16000 -s -o record.flac'+WAVE_OUTPUT_FILENAME)
	os.system('rm WAVE_OUTPUT_FILENAME')


def speech_recognition(file):
	os.system('wget -q -U "Mozilla/5.0" --post-file'+file+'--header "Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com.mx/speech-api/v2/recognize?output=json&lang=es&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw" | cut -d\\" -f8 > stt.txt')
	stt = open('stt.txt')
	line = stt.readline()
	stt.close()
	recognition = line.strip('\n')
	return recognition


tts = pttysx.init()
tts.say("Dear sir")
tts.say("I am janna your personal assistant")

while True:
	keyword= record()
	if keyword == "janna" || keyword == "Janna":
		
		tts.say("What can I do for you sir?")
		order = redord()
		print order
	pass



