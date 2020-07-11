# MLDatasetBuilder

**MLDatasetBuilder** is a python package that is helping to prepare images for your ML dataset. Whenever we begin a machine learning project, the first thing that we need is a dataset. Datasets will be the pillar of the training model. You can build the dataset either automatically or manually.


[![python version](https://img.shields.io/badge/Python-3.6-yellow)](https://pypi.org/project/MLDatasetBuilder/)
[![PyPI](https://img.shields.io/badge/pypi-v0.0.9-blue)](https://pypi.org/project/MLDatasetBuilder/)
[![Downloads](https://pepy.tech/badge/mldatasetbuilder)](https://pepy.tech/project/mldatasetbuilder)
[![Downloads](https://pepy.tech/badge/mldatasetbuilder/month)](https://pepy.tech/project/mldatasetbuilder/month)

**Author**: Karthick Nagarajan

**Email**: karthick965938@gmail.com

## Installation
We can install ***MLDatasetBuilder*** package using this command

```sh
pip install MLDatasetBuilder
```
### Available Operations

1) ***Remove*** unwanted format images and ***Rename*** image files

```sh
PrepareImage(folder_name, image_name)
#PrepareImage('images', 'dog')
```
2) ***Extract images from video file***
```sh
ExtractImages(video_path, filename, framesize)
#ExtractImages('video.mp4', 'frame', 10)
```

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

# Contact
MLDatasetBuilder was created by [Karthick Nagarajan](https://stackoverflow.com/users/6295641/karthick-nagarajan?tab=profile). Feel free to reach out on [Twitter](https://twitter.com/Karthick965938) or through [Email!](karthick965938@gmail.com)
