from keras.preprocessing import image
import numpy as np
import os

from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.models import Sequential,Model
from keras.layers import Flatten,Dropout,Dense,Activation
from keras.optimizers import SGD
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

data_dir = 'C:\\Users\\16520\\Desktop\\GenrePrediction\\img-data\\'

genres = ['ballad', 'mix', 'sad', 'happy']

num_classes = 4

data = []
label = []

for idx, subdir_name in enumerate(genres):
    sub_path = os.path.join(data_dir, subdir_name)

    for dirpath, dirnames, filenames in os.walk(sub_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            img = image.img_to_array(image.load_img(filepath))
            data.append(img)
            label.append([subdir_name])

ohe = OneHotEncoder()
data = np.array(data)
label = ohe.fit_transform(label).toarray()
label = np.array(label)

print(label)

model = InceptionResNetV2(include_top=False, weights='imagenet', input_shape=(299, 299, 3))

new_model = Sequential()
new_model.add(model)
new_model.add(Flatten())
new_model.add(Dense(1024, activation='relu'))
new_model.add(Dropout(0.2))
new_model.add(Dense(num_classes, activation='sigmoid'))
new_model.add(Activation('softmax'))

learning_rate = 0.01
epochs = 12
batch_size = 8      

opt = SGD(learning_rate=learning_rate, momentum=0.9)
new_model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])

X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.2, random_state=42)

new_model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(X_test, y_test))
