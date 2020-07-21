import os
import matplotlib
import pylab
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from PIL import Image

#matplotlib.use('Agg') # No pictures displayed 

genres = ['ballad', 'mix', 'sad', 'happy']
data_path = 'C:\\Users\\16520\\Desktop\\GenrePrediction\\data'

step = 5000
cut_len = 10000

for subdir_name in genres:
    sub_path = os.path.join(data_path, subdir_name)

    for dirpath, dirnames, filenames in os.walk(sub_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            fname = filename.split('.mp3')[0]
            mp3_content = AudioSegment.from_mp3(filepath)
            mp3_len = len(mp3_content)

            for s in range(0, mp3_len -cut_len + 1, step):
                mp3_cutted_content = mp3_content[s: s + cut_len + 1]
                mp3_cutted_content.export("tmp.mp3", format="mp3")
                pylab.axis('off') # no axis
                pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
                sig, fs = librosa.load("tmp.mp3")
                S = librosa.feature.melspectrogram(y=sig, sr=fs)
                librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
                save_path = 'C:\\Users\\16520\\Desktop\\GenrePrediction\\img-data\\' + subdir_name + '\\' + fname + str(s) +'.jpg'
                pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
                pylab.close()
                img = Image.open(save_path)
                img = img.resize((299, 299))
                img.save(save_path)
            