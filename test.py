from MLDatasetBuilder import *
# # Working
PrepareImage('test_assets/images', 'dog')
# # RenameFiles('rename_images', 'dog')
# ExtractImages('test_assets/dog.mp4', 'dog')

# import os

# basepath = 'test_assets'
# for fname in os.listdir(basepath):
#     path = os.path.join(basepath, fname)
#     if os.path.isfile(path):
#     	print('folder')
#     	print(path)
#         # skip directories
#         # continue
#     else:
#     	print('file')
#     	print(path)