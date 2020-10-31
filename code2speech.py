import pyttsx3
from pyttsx3 import voice
import time
import subprocess
import os


def textToWav(text, path):
    if os.path.exists(path):
        os.remove(path)
    subprocess.call(["espeak", "-w" + path, text])


def speak(text_file):
    with open(text_file, "r") as tf:
        text = tf.read()
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("rate", 5)
    engine.setProperty("volume", 1.0)
    engine.setProperty("voice", voices[16].id)
    lines = text.split("\n")
    lines = [line.strip("\n") for line in lines if line != ""]
    fname = text_file.replace(".txt", ".mp3")
    fname = fname.split("app/text/")[1]
    print(fname)
    mp3_path = os.path.join("app/static", fname)
    print(mp3_path)
    textToWav(text, mp3_path)
    # engine.save_to_file(text,mp3_path)
    engine.stop()
    return fname, text
