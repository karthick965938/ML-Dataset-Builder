import pathlib
import os
import time
# allow .jpg and .jpeg format only
def PrepareImage(dir, file_name=None):
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
# file rename operation
def RenameFiles(dir, file_name):
	os.getcwd()
	for i, filename in enumerate(os.listdir(dir)):
	  os.rename(dir + "/" + filename, dir + "/"+ file_name + str(i) + ".jpg")
def ExtractImages(video_file, filename, framesize):
	if not os.path.exists(filename):
    os.makedirs(filename)
	split_video(video_dir, filename, prefix=filename, step_size=framesize)
	time.sleep(5)
	rescale_images(filename, 800, 600)
def split_video(video_file, output_folder, prefix='frame', step_size=1):
  # Set step_size to minimum of 1
  if step_size <= 0:
    print('Invalid step_size for split_video; defaulting to 1')
    step_size = 1

  video = cv2.VideoCapture(video_file)

  count = 0
  index = 0
  # Loop through video frame by frame
  while True:
    ret, frame = video.read()
    if not ret:
      break
    # Save every step_size frames
    if count % step_size == 0:
      file_name = '{}{}.jpg'.format(prefix, index)
      cv2.imwrite(os.path.join(output_folder, file_name), frame)
      index += 1
    count += 1
  video.release()
  cv2.destroyAllWindows()

# change image resolution
def rescale_images(directory, height, width):
  for img in os.listdir(directory):
  	size = (height,width)
  	im = Image.open(directory+img)
  	im_resized = im.resize(size, Image.ANTIALIAS)
  	im_resized.save(directory+img)