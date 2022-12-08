import pandas as pd
import numpy as np 
import os
import shutil 
import itertools
import keras
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img 
from keras.models import Sequential 
from keras import optimizers
from keras.preprocessing import image
from keras.layers import Dropout, Flatten, Dense 
from keras import applications 
from keras.utils.np_utils import to_categorical 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
# %matplotlib inline
import math 
import datetime
import time
  
#Default dimensions we found online
img_width, img_height = 224, 224 
 
#Create a bottleneck file
top_model_weights_path = 'bottleneck_fc_model.h5'
#loading up our datasets
#bottlenecks are weights
train_data_dir = '/Users/ioannapapanikolaou/Documents/Year3/EPS/prep_dataset/train/'
validation_data_dir = '/Users/ioannapapanikolaou/Documents/Year3/EPS/prep_dataset/val/'
test_data_dir = '/Users/ioannapapanikolaou/Documents/Year3/EPS/prep_dataset/test/'

 
# number of epochs to train top model 
epochs = 7 #this has been changed after multiple model run 
# batch size used by flow_from_directory and predict_generator 
batch_size = 50 

#Loading vgc16 model
vgg16 = applications.VGG16(include_top=False, weights='imagenet')
datagen = ImageDataGenerator(rescale=1. / 255) 
 
#--------------------------------------------------------------------------------------------------------
# Creating the bottleneck files 
# # Train 
# generator_train = datagen.flow_from_directory( 
#     train_data_dir, 
#     target_size=(img_width, img_height), 
#     batch_size=batch_size, 
#     class_mode=None, 
#     shuffle=False) 
 
# nb_train_samples = len(generator_train.filenames) 
# num_classes = len(generator_train.class_indices) 
 
# predict_size_train = int(math.ceil(nb_train_samples / batch_size)) 
 
# bottleneck_features_train = vgg16.predict_generator(generator_train, predict_size_train) 
 
# np.save('bottleneck_features_train.npy', bottleneck_features_train)

# # Test
# generator_test = datagen.flow_from_directory( 
#     test_data_dir, 
#     target_size=(img_width, img_height), 
#     batch_size=batch_size, 
#     class_mode=None, 
#     shuffle=False) 
 
# nb_test_samples = len(generator_test.filenames) 
# num_classes = len(generator_test.class_indices) 
 
# predict_size_test = int(math.ceil(nb_test_samples / batch_size)) 
 
# bottleneck_features_test = vgg16.predict_generator(generator_test, predict_size_test) 
 
# np.save('bottleneck_features_test.npy', bottleneck_features_test)

# # Validation 
# generator_valid = datagen.flow_from_directory( 
#     validation_data_dir, 
#     target_size=(img_width, img_height), 
#     batch_size=batch_size, 
#     class_mode=None, 
#     shuffle=False) 
 
# nb_valid_samples = len(generator_valid.filenames) 
# num_classes = len(generator_valid.class_indices) 
 
# predict_size_valid = int(math.ceil(nb_valid_samples / batch_size)) 
 
# bottleneck_features_valid = vgg16.predict_generator(generator_valid, predict_size_valid) 
 
# np.save('bottleneck_features_valid.npy', bottleneck_features_valid)

#--------------------------------------------------------------------------------------------------------

# Load the bottleneck file for the data

#training data
generator_train_top = datagen.flow_from_directory( 
   train_data_dir, 
   target_size=(img_width, img_height), 
   batch_size=batch_size, 
   class_mode='categorical', 
   shuffle=False) 
 
nb_train_samples = len(generator_train_top.filenames) 
num_classes = len(generator_train_top.class_indices) 
 
# load the bottleneck features saved earlier 
train_data = np.load('bottleneck_features_train.npy') 
 
# get the class labels for the training data, in the original order 
train_labels = generator_train_top.classes 
 
# convert the training labels to categorical vectors 
train_labels = to_categorical(train_labels, num_classes=num_classes)

# Creating a bottleneck file for the testing data. (Same step for validation and testing):

#training data
generator_test_top = datagen.flow_from_directory( 
   test_data_dir, 
   target_size=(img_width, img_height), 
   batch_size=batch_size, 
   class_mode='categorical', 
   shuffle=False) 
 
nb_test_samples = len(generator_test_top.filenames) 
num_classes = len(generator_test_top.class_indices) 
 
# load the bottleneck features saved earlier 
test_data = np.load('bottleneck_features_test.npy') 
 
# get the class labels for the training data, in the original order 
test_labels = generator_test_top.classes 
 
# convert the training labels to categorical vectors 
test_labels = to_categorical(test_labels, num_classes=num_classes)

# Creating a bottleneck file for the validation data. (Same step for validation and testing):

#training data
generator_valid_top = datagen.flow_from_directory( 
   validation_data_dir, 
   target_size=(img_width, img_height), 
   batch_size=batch_size, 
   class_mode='categorical', 
   shuffle=False) 
 
nb_valid_samples = len(generator_valid_top.filenames) 
num_classes = len(generator_valid_top.class_indices) 
 
# load the bottleneck features saved earlier 
validation_data = np.load('bottleneck_features_valid.npy') 
 
# get the class labels for the training data, in the original order 
validation_labels = generator_valid_top.classes 
 
# convert the training labels to categorical vectors 
validation_labels = to_categorical(validation_labels, num_classes=num_classes)

# Creating the Convolutional Neural Network 

# start = datetime.datetime.now()
model = Sequential() 
model.add(Flatten(input_shape=train_data.shape[1:])) 
model.add(Dense(100, activation=keras.layers.LeakyReLU(alpha=0.3))) 
model.add(Dropout(0.5)) 
model.add(Dense(50, activation=keras.layers.LeakyReLU(alpha=0.3))) 
model.add(Dropout(0.3)) 
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss="categorical_crossentropy",
   optimizer=optimizers.RMSprop(lr=1e-4),
   metrics=['acc'])
history = model.fit(train_data, train_labels, 
   epochs=7,
   batch_size=batch_size, 
   validation_data=(validation_data, validation_labels))
model.save_weights(top_model_weights_path)
(eval_loss, eval_accuracy) = model.evaluate( 
    validation_data, validation_labels, batch_size=batch_size,     verbose=1)
print("[INFO] accuracy: {:.2f}%".format(eval_accuracy * 100)) 
print("[INFO] Loss: {}".format(eval_loss)) 
# end= datetime.datetime.now()
# elapsed= end-start
# print ("Time: ", elapsed)

# Visualization of the Accuracy and Loss
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(acc))
plt.plot(epochs, acc, 'r', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.ylabel('accuracy') 
plt.xlabel('epoch')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'r', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.ylabel('loss') 
plt.xlabel('epoch')
plt.legend()
plt.show()

model.evaluate(test_data, test_labels)

preds = np.round(model.predict(test_data),0)
print("rounded test_labels", preds)

# Testing 

def read_image(file_path):
    print("[INFO] loading and preprocessing image…") 
    image = load_img(file_path, target_size=(224, 224)) 
    image = img_to_array(image) 
    image = np.expand_dims(image, axis=0)
    image /= 255. 
    return image

def test_single_image(path):
    groceries_classes = ['Apple','Asparagus','Aubergine','Avocado','Banana','Brown-Cap-Mushroom','Cabbage','Carrots','Cucumber','Garlic',
'Ginger','Juice','Kiwi','Leek','Lemon','Lime','Mango','Melon','Milk','Nectarine','Oat-Milk','Oatghurt','Onion',
'Orange','Papaya','Passion-Fruit','Peach','Pear','Pepper','Pineapple','Plum','Pomegranate','Potato','Red-Beet',
'Red-Grapefruit','Satsumas','Sour-Cream','Sour-Milk','Soy-Milk','Soyghurt','Tomato','Yoghurt','Zucchini']
    image = read_image(path)
    time.sleep(.5)
    bt_prediction = vgg16.predict(image) 
    preds = model.predict_proba(bt_prediction)
    for idx, grocery, x in zip(range(0,6), groceries_classes , preds[0]):
        print("ID: {}, Label: {} {}%".format(idx, grocery, round(x*100,2) ))
    print("Final Decision:")
    time.sleep(.5)
    for x in range(3):
        print('.'*(x+1))
        time.sleep(.2)
    class_predicted = model.predict_classes(bt_prediction)
    class_dictionary = generator_test_top.class_indices 
    inv_map = {v: k for k, v in class_dictionary.items()} 
    print("ID: {}, Label: {}".format(class_predicted[0],  inv_map[class_predicted[0]])) 
    return load_img(path)


path = '/Users/ioannapapanikolaou/Documents/Year3/EPS/prep_dataset/test/Ginger/Ginger_005.jpg'
test_single_image(path)

