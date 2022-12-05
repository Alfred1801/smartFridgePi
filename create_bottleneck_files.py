#Default dimensions we found online
img_width, img_height = 224, 224 
 
#Create a bottleneck file
top_model_weights_path = 'bottleneck_fc_model.h5'
# loading up our datasets

train_data_dir = '/Users/ioannapapanikolaou/Documents/Year3/EPS/prep_dataset/train/'
validation_data_dir = '/Users/ioannapapanikolaou/Documents/Year3/EPS/prep_dataset/val/'
test_data_dir = '/Users/ioannapapanikolaou/Documents/Year3/EPS/prep_dataset/test/'


# batch size used by flow_from_directory and predict_generator 
batch_size = 50 

#Loading vgc16 model
vgg16 = applications.VGG16(include_top=False, weights='imagenet')
datagen = ImageDataGenerator(rescale=1. / 255) 
 
# Train 
generator_train = datagen.flow_from_directory( 
    train_data_dir, 
    target_size=(img_width, img_height), 
    batch_size=batch_size, 
    class_mode=None, 
    shuffle=False) 
 
nb_train_samples = len(generator_train.filenames) 
num_classes = len(generator_train.class_indices) 
 
predict_size_train = int(math.ceil(nb_train_samples / batch_size)) 
 
bottleneck_features_train = vgg16.predict_generator(generator_train, predict_size_train) 
 
np.save('bottleneck_features_train.npy', bottleneck_features_train)

# Test
generator_test = datagen.flow_from_directory( 
    test_data_dir, 
    target_size=(img_width, img_height), 
    batch_size=batch_size, 
    class_mode=None, 
    shuffle=False) 
 
nb_test_samples = len(generator_test.filenames) 
num_classes = len(generator_test.class_indices) 
 
predict_size_test = int(math.ceil(nb_test_samples / batch_size)) 
 
bottleneck_features_test = vgg16.predict_generator(generator_test, predict_size_test) 
 
np.save('bottleneck_features_test.npy', bottleneck_features_test)

# Validation 
generator_valid = datagen.flow_from_directory( 
    validation_data_dir, 
    target_size=(img_width, img_height), 
    batch_size=batch_size, 
    class_mode=None, 
    shuffle=False) 
 
nb_valid_samples = len(generator_valid.filenames) 
num_classes = len(generator_valid.class_indices) 
 
predict_size_valid = int(math.ceil(nb_valid_samples / batch_size)) 
 
bottleneck_features_valid = vgg16.predict_generator(generator_valid, predict_size_valid) 
 
np.save('bottleneck_features_valid.npy', bottleneck_features_valid)