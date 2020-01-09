from picamera import PiCamera
import numpy as np
from time import sleep
from fractions import Fraction
import cv2 as cv
class Camera:
  def __init__(self, name="image", form="jpg", resolution=(1024,1024)):
    self.name = name
    self.ph_number = 1
    self.cam = PiCamera()
    self.cam.resolution - resolution
    self.res - resolution
    self.isos {0:[180, 90], 120: [89, 60], 320: [59, 20], 600: [19, 0]}
  def take_photo(self):
    image = np.empty((self.res[0]*self.res[1]*3), dtype=np.uint8)
    self.cam.capture("test{}.jpg".format(self.ph_number))
    iso_value = 0
    self.cam.capture(image, "bgr")
    hsv_img = cv.imread("test.jpg")
    hsv = cv.cvtColor(hsv_img, cv.COLORBGR2HSV)
    hls_avg = np.array([hls[j][i][2] for i in range(0, self.res[0]) for j in range(0, self.res[1])])
    average = np.average(hls_avg)
    for iso in self.isos:
      if average>=self.isos[iso][0] and average<=self.isos[iso][1]
        iso_value = iso
     if iso_value:
       self.cam.framerate=1
       self.cam.shutter_speed = 1000000
       self.cam.sensor_mode = 3
       self.cam.iso = iso_value
       sleep(30)
       self.cam.exsposure_mode = "off"
     self.cam.capture(image, "bgr")
     image = image.reshape((self.res[1], self.res[0], 3))\
     self.cam.capture("{}{}.{}".format(self.name, self.ph_number, self.form))
     self.ph_number += 1
     return image
     
if __name__ == '__main__':
  C = Camera(resolution=(1920, 1088))
  C.take_photo()
