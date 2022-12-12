import pandas as pd
import numpy as np 
import os
import shutil 
import itertools
import keras
import time
from keras import applications 

class ProductDetector:
    model=object
    def __init__(self):
        reconstructedModel = keras.models.load_model("my_model.h5")
        reconstructedModel.load_weights("bottleneck_fc_model.h5")
        self.model=reconstructedModel
        self.class_dictionary = {'Apple': 0,
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
        self.groceries_classes = ['Apple','Asparagus','Aubergine','Avocado','Banana','Mushroom','Cabbage','Carrots','Cucumber','Garlic',
        'Ginger','Juice','Kiwi','Leek','Lemon','Lime','Mango','Melon','Milk','Nectarine','Oat-Milk','Oatghurt','Onion',
        'Orange','Papaya','Passion-Fruit','Peach','Pear','Pepper','Pineapple','Plum','Pomegranate','Potato','Red-Beet',
        'Red-Grapefruit','Satsumas','Sour-Cream','Sour-Milk','Soy-Milk','Soyghurt','Tomato','Yoghurt','Zucchini']
        self.vgg16 = applications.VGG16(include_top=False, weights='imagenet')

    
    def productGuess(self, frame):
        image=frame.resize(224,224)
        time.sleep(.5)
        bt_prediction = self.vgg16.predict(image) 
        preds = self.model.predict(bt_prediction)
        for idx, grocery, x in zip(range(0,6), self.groceries_classes , preds[0]):
            print("ID: {}, Label: {} {}%".format(idx, grocery, round(x*100,2) ))
        print("Final Decision:")
        time.sleep(.5)
        for x in range(3):
            print('.'*(x+1))
            time.sleep(.2)
        class_predicted = np.argmax(self.model.predict(bt_prediction), axis=-1)
        inv_map = {v: k for k, v in self.class_dictionary.items()} 
        print("ID: {}, Label: {}".format(class_predicted[0],  inv_map[class_predicted[0]])) 
        return inv_map[class_predicted[0]]

    def productGuesses(self,frames)-> list :
        products=[]
        for frame in frames:
            guess=self.productGuess(self,frame)
            if guess not in products:
                products =+ guess
        return products 

    