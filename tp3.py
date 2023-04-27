#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

drawing = 0
coordenadas = []
 
img = cv2.imread('images\SRC.jpg')
img1 = cv2.imread('images\SRC.jpg')
img2 = np.zeros(img.shape, dtype='uint8')

rowsSrc, colsSrc = img.shape[:2]

output_pts = np.float32([[0,0], [colsSrc-1,0], [colsSrc-1,rowsSrc-1], [0,rowsSrc-1]])
input_pts = []

def draw_rectangle(event, x, y, flags, param):
 global drawing
 
 if event == cv2.EVENT_LBUTTONDOWN:
  global img, img2  
  
  coordenadas.append([x,y])
  drawing += 1
  cv2.circle(img, (x, y), 4 ,(0, 255, 0), -1)
  
 if drawing == 4: 
   
   input_pts = np.float32(coordenadas)
   
   M = cv2.getPerspectiveTransform(input_pts, output_pts)
   dst = cv2.warpPerspective(img1, M, (colsSrc,rowsSrc))
   cv2.imwrite('images/resultado_tp3.jpg', dst)
   
   img = dst
   drawing = 0
   coordenadas.clear()
   
       

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

while(1):
 cv2.imshow('image', img)
 k = cv2.waitKey(1) & 0xFF
 
 if k == ord('q'):
  break
cv2.destroyAllWindows()
