import cv2
import os

IMAGE_PATH = 'path'
RESIZE_PATH = 'path'
      
#! RESIZE
def resize_image(image, height = 1200, width = 800):
  top, bottom, left, right = (0,0,0,0)   
  h, w, _ = image.shape   
  longest_edge = max(h,w)
  
  if h < longest_edge:
    dh = longest_edge - h
    top = dh // 2
    bottom = dh - top
  elif w < longest_edge:
    dw = longest_edge - w
    left = dw // 2
    right = dw - left
  else:
    pass 
  
  # RGB  
  BLACK = [0,0,0]   
  constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value = BLACK)
  return cv2.resize(constant, (height, width))

#! read__image
def read__image(path_name):
  num = 0 
  for dir_image in os.listdir(path_name): # os.listdir()                            
    full_path = os.path.abspath(os.path.join(path_name,dir_image)) 
    
    if os.path.isdir(full_path):
      trainingData = []
    else:  
      if dir_image.endswith('.JPG', 'jpg'):
        image = cv2.imread(full_path)
        image = resize_image(image)
        resize_path = RESIZE_PATH
        name = os.path.basename(full_path)[:-4]
        image_name = os.path.join(resize_path, name+'.jpg')
      
        cv2.imwrite(image_name, image)
        

if __name__=='__main__':
  read__image(IMAGE_PATH)
