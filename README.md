# MLDatasetBuilder

**MLDatasetBuilder** is a python package which is help to prepare image for your ML dataset.Whenever we begin a machine learning project, the first thing that we need is a dataset. Dataset will be the pillar of training model. You can build the dataset either automatically or manually.

[![python version](https://img.shields.io/badge/Python-3.6-yellow)](https://pypi.org/project/MLDatasetBuilder/)
[![PyPI](https://img.shields.io/badge/pypi-v0.0.3-blue)](https://pypi.org/project/MLDatasetBuilder/)


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

### How to use this package

we can get images from Google. Using the [Download All Images](https://chrome.google.com/webstore/detail/download-all-images/ifipmflagepipjokmbdecpmjbibjnakm?hl=en) browser extension we can easily get images in a few minutes. You can check out [here](https://www.youtube.com/watch?v=ik1VxrtN7m8&feature=youtu.be) for more details about this extension!


![logo](https://github.com/karthick965938/ML-Dataset-Builder/blob/master/assets/step_01.gif)

# Contact
MLDatasetBuilder was created by [Karthick Nagarajan](https://stackoverflow.com/users/6295641/karthick-nagarajan?tab=profile). Feel free to reach out on [Twitter](https://twitter.com/Karthick965938) or through [Email!](karthick965938@gmail.com)
