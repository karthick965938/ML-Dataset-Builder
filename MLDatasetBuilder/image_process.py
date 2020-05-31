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