import pathlib
import os
import time
import cv2
from PIL import Image
from art import *
from termcolor import colored, cprint
from progress.bar import ShadyBar

# ASCI LOGO
text = colored(text2art("MLDatasetBuilder"), 'blue')

# allow .jpg and .jpeg format only
def PrepareImage(dir, file_name=None):
  print(text)
  bar = ShadyBar('Image  Processing', max=len(os.listdir(dir)))
  for i, file in enumerate(os.listdir(dir)):
    path = pathlib.Path(dir + "/" + file)
    if os.path.isfile(path):
      if (path.suffix != '.jpg' and path.suffix != '.jpeg'):
        path.unlink()
    time.sleep(0.005)
    bar.next()
  bar.finish()
  time.sleep(2)
  if file_name is None:
    file_name = time.strftime("%Y-%m-%d-%H-%M-%S")
    RenameFiles(dir, file_name)
  else:
    RenameFiles(dir, file_name)
# file rename operation
def RenameFiles(dir, file_name):
  os.getcwd()
  bar = ShadyBar('Rename Processing', max=len(os.listdir(dir)))
  for i, filename in enumerate(os.listdir(dir)):
    path = pathlib.Path(dir + "/" + filename)
    if os.path.isfile(path):
      os.rename(dir + "/" + filename, dir + "/"+ file_name + str(i) + ".jpg")
    time.sleep(0.005)
    bar.next()
  bar.finish()
# Extract images from the video
def ExtractImages(video_file, filename, framesize=5):
  if not os.path.exists(filename):
    os.makedirs(filename)
  frames_to_video(video_file, filename, framesize)
  time.sleep(2)
  rescale_images(filename, 800, 600)
def frames_to_video(inputpath, outputpath, fps=5):
  print(text)
  cap = cv2.VideoCapture(inputpath)
  count = 0
  index = 0
  length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
  bar = ShadyBar('Image Create Processing', max=video_frame_count(length, fps))
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
    time.sleep(0.005)
    bar.next()
  bar.finish()
def video_frame_count(length, fps):
  if length % fps == 0:
    return length / fps
  else:
    return length//fps + 1
# change image resolution
def rescale_images(directory, height, width):
  bar = ShadyBar('Image Resize Processing', max=len(os.listdir(directory)))
  for img in os.listdir(directory):
    size = (height,width)
    im = Image.open(directory+'/'+img)
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save(directory+'/'+img)
    time.sleep(0.005)
    bar.next()
  bar.finish()
def MLDatasetBuilder():
  text = colored(text2art("MLDatasetBuilder"), 'blue')
  print(text)
  print(colored('Welcome to MLDatasetBuilder ', 'blue') + colored(':)', 'blue', attrs=['blink']))
  print(colored('Available Operations ', 'blue') + colored(':-', 'blue', attrs=['blink']))
  print(colored('1) PrepareImage', 'grey', attrs=['bold']) + colored(' --> ', 'grey', attrs=['blink']) + colored('Remove unwanted format images and Rename image files.', 'blue', attrs=['bold']))
  print("   " + colored('#PrepareImage(folder_name, image_name)', 'grey', attrs=['bold']))
  print("   " + colored("PrepareImage('images', 'dog')", 'grey', attrs=['bold']))
  print(colored('2) ExtractImages', 'grey', attrs=['bold']) + colored(' --> ', 'grey', attrs=['blink']) + colored('Extract images from video file', 'blue', attrs=['bold']))
  print("   " + colored('#ExtractImages(video_path, file_name, frame_size)', 'grey', attrs=['bold']))
  print("   " + colored("ExtractImages('video.mp4', 'frame', 10)", 'grey', attrs=['bold']))
