import pathlib
import os
import time
import cv2
from PIL import Image
# allow .jpg and .jpeg format only
def PrepareImage(dir, file_name=None):
  print('Image Process Start')
  for i, file in enumerate(os.listdir(dir)):
    path = pathlib.Path(dir + "/" + file)
    if (path.suffix != '.jpg' and path.suffix != '.jpeg'):
      path.unlink()
  time.sleep(5)
  if file_name is None:
    file_name = time.strftime("%Y-%m-%d-%H-%M-%S")
    RenameFiles(dir, file_name)
  else:
    RenameFiles(dir, file_name)
  print('Image Process End')
# file rename operation
def RenameFiles(dir, file_name):
	os.getcwd()
	for i, filename in enumerate(os.listdir(dir)):
	  os.rename(dir + "/" + filename, dir + "/"+ file_name + str(i) + ".jpg")
# Extract images from the video
def ExtractImages(video_file, filename, framesize=5):
  if not os.path.exists(filename):
    os.makedirs(filename)
  frames_to_video(video_file, filename, framesize)
  time.sleep(5)
  rescale_images(filename, 800, 600)
def frames_to_video(inputpath, outputpath, fps=5):
  cap = cv2.VideoCapture(inputpath)
  count = 0
  index = 0

  print('Image Create Process Start')
  while cap.isOpened():
    ret, frame = cap.read()
    if ret:
      name = outputpath + str(index) + '.jpg'
      cv2.imwrite(os.path.join(outputpath, name), frame)
      count += fps # i.e. at 30 fps, this advances one second
      index += 1
      cap.set(1, count)
    else:
      cap.release()
      break
  print('Image Create Process End')
# change image resolution
def rescale_images(directory, height, width):
  print('Image Resize Process Start')
  for img in os.listdir(directory):
    size = (height,width)
    im = Image.open(directory+'/'+img)
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save(directory+'/'+img)
  print('Image Resize Process End')