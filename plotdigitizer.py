import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import cv2
import numpy as np

def do_magic(img, color, dots):
    
    return("IT'S REAL MAGIC!")
    

def euclidean(tup1, tup2):
  return ((int(tup1[0])-int(tup2[0]))**2 + (int(tup1[1])-int(tup2[1]))**2 + (int(tup1[2])-int(tup2[2]))**2)**0.5


def points(image, color, dots):

  img = image[:, :, [2, 1, 0]]
  edges = cv2.Canny(img, 100, 200)

  distance = 30


  start_x = 0
  start_y = 0

  X = []
  Y = []

  for i in range(0, len(img), 6):
    for j in range(0, len(img[i]), 6):
      if euclidean(tuple(img[i, j]), color) < distance:
        X.append(j)
        Y.append(i)

  dataset = []

  for i in range(len(Y)):
    Y[i] = len(img) - Y[i]
    dataset.append((X[i], Y[i]))
  
  return dataset


def line(image, color, dots):
  
  img = image[:, :, [2, 1, 0]]
  edges = cv2.Canny(img, 100, 200)

  distance = 60

  middle_x = len(img[0]) // 2
  start_y = 0
  for i in range(1, len(edges)):
    if edges[-i, middle_x] == 255:
      start_y = len(edges) - i - 1
      break
  start_y -= 5

  start_x = middle_x

  while edges[start_y, start_x] == 0:
    start_x -= 1

  i = start_y-5
  j = middle_x
  while edges[i, j] == 0:
    i -= 1

  begin_y = i
  begin_x = j


  X = []
  Y = []
  Y2 = [begin_y]
  X2 = [begin_x]
  y = begin_y
  x = begin_x
  end = False
  while not end:
    x += 1
    y = Y2[-1]
    for i in range(10):
      end = x == len(edges[0]-start_x)
      if end:
        break
      if edges[y-i,x] == 255 and euclidean(tuple(img[y-i, x]), color) < distance:
        Y2.append(y-i)
        X2.append(x)
        break
      if edges[y+i,x] == 255 and euclidean(tuple(img[y+i, x]), color) < distance:
        Y2.append(y+i)
        X2.append(x)
        break

  Y1 = [begin_y]
  X1 = [begin_x]
  y = begin_y
  x = begin_x
  end = False
  while not end:
    x -= 1
    y = Y1[-1]
    for i in range(10):
      end = x == start_x
      if end:
        break
      if edges[y-i,x] == 255 and euclidean(tuple(img[y-i, x]), color) < distance:
        Y1.append(y-i)
        X1.append(x)
        break
      if edges[y+i,x] == 255 and euclidean(tuple(img[y+i, x]), color) < distance:
        Y1.append(y+i)
        X1.append(x)
        break
  Y1.reverse()
  X1.reverse()

  X = X1 + X2
  Y = Y1 + Y2

  dataset = []

  for i in range(len(Y)):
    Y[i] = len(img) - Y[i]
    dataset.append((X[i], Y[i]))
  
  return dataset


def barplot(image, color, dots):

  img = image[:, :, [2, 1, 0]]
  edges=  cv2.Canny(img, 100, 200)

  distance = 60


  bg = bars[0]
  plot = bars[1]

  start_x = 0
  start_y = 0

  for i in range(len(img)):
    for j in range(len(img[i])):
      if euclidean(tuple(img[i, j]), color) < distance:
        start_y = i
        start_x = j
        break
  start_y -= 5

  white = False
  middle = 0
  simple_linear_interpolation = 0
  for j in range(start_x, len(img[start_y])):
    if not white:
      white = euclidean(tuple(img[start_y, j]), (255,255,255)) < distance
    if middle == 0 and white:
      middle = (start_x + j) // 2
    if white and euclidean(tuple(img[start_y, j]), color) < distance:
      step = j - start_x
      break


  dataset=[]


  mid = middle
  while mid + step < len(img[0]):
    for i in range(len(img)):
      if euclidean(tuple(img[i, mid]), color) < distance:
        dataset.append(i)
        break
      img[i, mid] = [255,0,0]
    mid += step


  for i in range(len(dataset)):
    dataset[i] = len(img) - dataset[i]

  return dataset
  
  
def line_filled(image, color, dots):

  img = image[:, :, [2, 1, 0]]
  edges=  cv2.Canny(img, 100, 200)


  distance = 30


  middle_x = len(img[0]) // 2
  start_y = 0
  for i in range(1, len(edges)):
    if edges[-i, middle_x] == 255:
      start_y = len(edges) - i - 1
      break
  start_y -= 5

  start_x = middle_x

  while edges[start_y, start_x] == 0:
    start_x -= 1

  i = start_y-5
  j = middle_x
  while edges[i, j] == 0:
    i -= 1
  begin_y = i
  begin_x = j


  Y2 = [begin_y]
  X2 = [begin_x]
  y = begin_y
  x = begin_x
  end = False
  while not end:
    x += 1
    y = Y2[-1]
    for i in range(10):
      end = x == len(edges[0]-start_x)
      if end:
        break
      if edges[y-i,x] == 255 and euclidean(tuple(img[y-i, x]), color) < distance:
        Y2.append(y-i)
        X2.append(x)
        break
      if edges[y+i,x] == 255 and euclidean(tuple(img[y+i, x]), color) < distance:
        Y2.append(y+i)
        X2.append(x)
        break

  Y1 = [begin_y]
  X1 = [begin_x]
  y = begin_y
  x = begin_x
  end = False
  while not end:
    x -= 1
    y = Y1[-1]
    for i in range(10):
      end = x == start_x
      if end:
        break
      if edges[y-i,x] == 255 and euclidean(tuple(img[y-i, x]), color) < distance:
        Y1.append(y-i)
        X1.append(x)
        break
      if edges[y+i,x] == 255 and euclidean(tuple(img[y+i, x]), color) < distance:
        Y1.append(y+i)
        X1.append(x)
        break
  Y1.reverse()
  X1.reverse()

  X = X1 + X2
  Y = Y1 + Y2

  dataset = []

  for i in range(len(Y)):
    Y[i] = len(img) - Y[i]
    dataset.append((X[i], Y[i]))

  return dataset
