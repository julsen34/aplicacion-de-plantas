import numpy as np
import tensorflow as tf
import keras as tf
from keras.api.preprocessing.image import load_img, img_to_array

def predict_image(model, img_path):
    img = load_img(img_path, target_size=(150, 150))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    predictions = model.predict(img_array)
    return predictions
