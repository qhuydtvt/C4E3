import threading
import os, sys
import time
import winsound
import random
import logging
from PIL import Image
dir_image = os.listdir("D:\hinhanh")
dir_wav = os.listdir("D:\wav")
def moimage(dir_image,image_point):
    image = random.choice(dir_image)
    im = Image.open("D:\hinhanh"+ image)
    im.show()
    image_point.wait()
def mowav(dir_wav, image_point):
    image_point = threading.Event()
    while not image_point.is_set():
        image_point_set = image_point.wait()
        if image_point_set:
            wav_random = random.choice(dir_wav)
            winsound.PlaySound("D:\wav/" + wav_random, winsound.SND_FILENAME)
        else:
            continue
class mythread(threading.Thread):
    def __init__(self, dir_image,dir_wav,image_point):
        threading.Thread.__init__(self)
        self.dir_image = dir_image
        self.dir_wav = dir_wav
        self.image_point = image_point
    def run(self):
        self.image_point = threading.Event()
        imagethread = threading.Thread(target=moimage(dir_image,image_point=1))
        imagethread.start()
        audiothread = threading.Thread(target= mowav(dir_wav,image_point=0))
        while True:
            i = 0
            audiothread.start()
            self.image_point.set()
            time.sleep(300)
            i += 1
            if i == 1:
                continue
t = mythread(dir_image,dir_wav,image_point=1)
t.start()