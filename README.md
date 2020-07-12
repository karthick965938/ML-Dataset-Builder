# MLDatasetBuilder

**[MLDatasetBuilder-Version 1.0.0](https://pypi.org/project/MLDatasetBuilder/)** - A Python package to build Dataset for Machine Learning
Whenever we begin a machine learning project, the first thing that we need is a dataset. Datasets will be the pillar of the training model. You can build the dataset either automatically or manually. MLDatasetBuilder is a python package which is helping to prepare the image for your ML dataset.


[![python version](https://img.shields.io/badge/Python-3.6-yellow)](https://pypi.org/project/MLDatasetBuilder/)
[![PyPI](https://img.shields.io/badge/pypi-v1.0.0-blue)](https://pypi.org/project/MLDatasetBuilder/)
[![Downloads](https://pepy.tech/badge/mldatasetbuilder)](https://pepy.tech/project/mldatasetbuilder)
[![Downloads](https://pepy.tech/badge/mldatasetbuilder/month)](https://pepy.tech/project/mldatasetbuilder/month)

**Author**: Karthick Nagarajan

**Email**: karthick965938@gmail.com

## Installation
We can install ***MLDatasetBuilder*** package using this command

```sh
pip install MLDatasetBuilder
```

### How to test?
When you run python3 in the terminal, it will produce output like this:

```sh
Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Run the following code to you can get the Initialize process output for the MLDatasetBuilder package.

```sh
>>> from MLDatasetBuilder import *
>>> MLDatasetBuilder()
```
![package_sample_output](https://i1.wp.com/cdn-images-1.medium.com/max/800/1*h4KOBQoEjCaoUWjj0PzVjg.gif?ssl=1)

### Available Operations

1) ***Remove*** unwanted format images and ***Rename*** image files

```sh
#PrepareImage(folder_name, image_name)
PrepareImage('images', 'dog')
```
2) ***Extract images from video file***
```sh
#ExtractImages(video_path, file_name, frame_size)
ExtractImages('video.mp4', 'frame', 10)
#OR
#ExtractImages(video_path, filename)
ExtractImages('video.mp4', 'frame')
#Default FPS will be 5
```

## Step1 — Get images from google

### Remove unwanted format images and Rename image files

we can get images from Google. Using the [Download All Images](https://chrome.google.com/webstore/detail/download-all-images/ifipmflagepipjokmbdecpmjbibjnakm?hl=en) browser extension we can easily get images in a few minutes. You can check out [here](https://www.youtube.com/watch?v=ik1VxrtN7m8&feature=youtu.be) for more details about this extension!


![step_1](https://raw.githubusercontent.com/karthick965938/ML-Dataset-Builder/master/assets/step_01.gif)

Once you have downloaded the images using this extension, you can create a python file called ***test_python_file.py*** the same directory as below.

```sh
download_image_folder/
   _14e839ba-9691-11ea-a968-2ed746e9a968.jpg
   5e5f7af12600004018b602c0.jpeg
   A471529_Alice_b-1.jpg
   image1.png
   image2.png
   ...
test_python_file.py
```
Inside the images folder, you can see lots of png images and random filenames.


```sh
PrepareImage(folder_name, image_name)
#PrepareImage('images', 'dog')
```

```sh
download_image_folder/
   dog_0.jpg
   dog_1.jpg
   dog_2.jpg
   dog_3.png
   dog_4.png
   ...
test.py
```
![step_1](https://raw.githubusercontent.com/karthick965938/ML-Dataset-Builder/master/assets/step_2.gif)

This process very helps to annotate your images while labeling. And of course, it will be like one of the standardized things.


### Extract images from video file

```sh
download_image_folder/
video.mp4
test.py
```

```sh
ExtractImages(video_path, folder_name, framesize)
#ExtractImages('video.mp4', 'frame', 10)
ExtractImages(video_path, folder_name)
#ExtractImages('video.mp4', 'frame')
```


```sh
download_image_folder/
dog/
   dog_0.jpg
   dog_1.jpg
   dog_2.jpg
   dog_3.png
   dog_4.png
   ...
dog.mp4
test.py
```

![step_1](https://raw.githubusercontent.com/karthick965938/ML-Dataset-Builder/master/assets/step_3.gif)

# Contributing
All issues and pull requests are welcome! To run the code locally, first, fork the repository and then run the following commands on your computer:

```sh
git clone https://github.com/<your-username>/ML-Dataset-Builder.git
cd ML-Dataset-Builder
# Recommended creating a virtual environment before the next step
pip3 install -r requirements.txt
```
When adding code, be sure to write unit tests where necessary.

# Contact
MLDatasetBuilder was created by [Karthick Nagarajan](https://stackoverflow.com/users/6295641/karthick-nagarajan?tab=profile). Feel free to reach out on [Twitter](https://twitter.com/Karthick965938) or through [Email!](karthick965938@gmail.com)
