import pandas as pd
import numpy as np 
import os
import shutil 
import itertools
import keras
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from keras.preprocessing.image import ImageDataGenerator #img_to_array , load_img
from tensorflow.keras.utils import img_to_array , load_img
from keras.models import Sequential 
from keras import optimizers
from keras.preprocessing import image
from keras.layers import Dropout, Flatten, Dense 
from keras import applications 
from keras.utils.np_utils import to_categorical 
#import matplotlib.pyplot as plt 
#import matplotlib.image as mpimg
# %matplotlib inline
import math 
import datetime
import time
  
def CNN_init():
    reconstructedModel = keras.models.load_model("my_model.h5")
    reconstructedModel.load_weights("bottleneck_fc_model.h5")
    return reconstructedModel

def read_image(file_path):
    print("[INFO] loading and preprocessing image…") 
    image = load_img(file_path, target_size=(224, 224)) 
    image = img_to_array(image) 
    image = np.expand_dims(image, axis=0)
    image /= 255. 
    return image
    
def test_single_image(path, model):
    reconModel = keras.models.load_model("my_model.h5")
    reconModel.load_weights("bottleneck_fc_model.h5")
    vgg16 = applications.VGG16(include_top=False, weights='imagenet')
    groceries_classes = ['Apple','Asparagus','Aubergine','Avocado','Banana','Mushroom','Cabbage','Carrots','Cucumber','Garlic',
'Ginger','Juice','Kiwi','Leek','Lemon','Lime','Mango','Melon','Milk','Nectarine','Oat-Milk','Oatghurt','Onion',
'Orange','Papaya','Passion-Fruit','Peach','Pear','Pepper','Pineapple','Plum','Pomegranate','Potato','Red-Beet',
'Red-Grapefruit','Satsumas','Sour-Cream','Sour-Milk','Soy-Milk','Soyghurt','Tomato','Yoghurt','Zucchini']

    #datagen = ImageDataGenerator(rescale=1. / 255)

    #generator_test_top = datagen.flow_from_directory( 
    #test_data_dir, 
    #target_size=(img_width, img_height), 
    #batch_size=batch_size, 
    #class_mode='categorical', 
    #shuffle=False) 

    class_dictionary = {'Apple': 0,
    'Asparagus': 1,
    'Aubergine': 2,
    'Avocado': 3,
    'Banana': 4,
    'Cabbage': 5,
    'Carrots': 6,
    'Cucumber': 7,
    'Garlic': 8,
    'Ginger': 9,
    'Juice': 10,
    'Kiwi': 11,
    'Leek': 12,
    'Lemon': 13,
    'Lime': 14,
    'Mango': 15,
    'Melon': 16,
    'Milk': 17,
    'Mushroom': 18,
    'Nectarine': 19,
    'Oat-Milk': 20,
    'Oatghurt': 21,
    'Onion': 22,
    'Orange': 23,
    'Papaya': 24,
    'Passion-Fruit': 25,
    'Peach': 26,
    'Pear': 27,
    'Pepper': 28,
    'Pineapple': 29,
    'Plum': 30,
    'Pomegranate': 31,
    'Potato': 32,
    'Red-Beet': 33,
    'Red-Grapefruit': 34,
    'Satsumas': 35,
    'Sour-Cream': 36,
    'Sour-Milk': 37,
    'Soy-Milk': 38,
    'Soyghurt': 39,
    'Tomato': 40,
    'Yoghurt': 41,
    'Zucchini': 42 }
    image = read_image(path)
    time.sleep(.5)
    bt_prediction = vgg16.predict(image) 
    #preds = reconModel.predict_proba(bt_prediction)
    preds = reconModel.predict(bt_prediction)
    for idx, grocery, x in zip(range(0,6), groceries_classes , preds[0]):
        print("ID: {}, Label: {} {}%".format(idx, grocery, round(x*100,2) ))
    print("Final Decision:")
    time.sleep(.5)
    for x in range(3):
        print('.'*(x+1))
        time.sleep(.2)
    #class_predicted = reconModel.predict_classes(bt_prediction)
    class_predicted = np.argmax(reconModel.predict(bt_prediction), axis=-1)
    inv_map = {v: k for k, v in class_dictionary.items()} 
    print("ID: {}, Label: {}".format(class_predicted[0],  inv_map[class_predicted[0]])) 
    return inv_map[class_predicted[0]]