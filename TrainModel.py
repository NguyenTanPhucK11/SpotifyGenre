import tensorflow as tf
from PIL import Image
import numpy as np
import os

data_dir = 'C:\\Users\\16520\\Desktop\\GenrePrediction\\img-data\\'

genres = ['ballad', 'mix', 'sad', 'happy']

data = []
label = []

for idx, subdir_name in enumerate(genres):
    sub_path = os.path.join(data_dir, subdir_name)

    for dirpath, dirnames, filenames in os.walk(sub_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            img = Image.open(filepath)
            data.append(img)
            label.append(idx)

data = np.array(data).astype(np.float32)
label = np.array(label).astype(np.float32)
t 