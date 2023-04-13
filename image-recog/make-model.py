import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras import datasets, layers, models
rgb_lim = 255
(train_images, train_labels), (test_images, test_labels) = datasets.cifar100.load_data()
train_images = train_images / 255
test_images = test_images / 255
allow = [0, 9, 10, 16, 29, 53, 57, 61]
names = ['apples', 'bottles', 'bowls', 'cans', 'cups', 'oranges', 'pears', 'plates']
s = """beaver, dolphin, otter, seal, whale, aquarium fish, flatfish, ray, shark, trout, 
orchids, poppies, roses, sunflowers, tulips, bottles, bowls, cans, cups, plates, 
apples, mushrooms, oranges, pears, sweet peppers, clock, computer keyboard, lamp, telephone, television, 
bed, chair, couch, table, wardrobe, bee, beetle, butterfly, caterpillar, cockroach, bear, leopard, lion, tiger, wolf, 
bridge, castle, house, road, skyscraper, cloud, forest, mountain, plain, sea, camel, cattle, chimpanzee, 
elephant, kangaroo, fox, porcupine, possum, raccoon, skunk, crab, lobster, snail, spider, worm, 
baby, boy, girl, man, woman, crocodile, dinosaur, lizard, snake, turtle, hamster, 
mouse, rabbit, shrew, squirrel, maple, oak, palm, pine, willow, bicycle, bus, motorcycle, pickup, truck, train, 
lawm-mower, rocket, streetcar, tank, tractor"""
s = s.replace("\n", "")
class_names = s.split(", ")
class_names.sort()
train_images_nice = []
train_labels_nice = []
test_images_nice = []
test_labels_nice = []
print(type(train_images[0]))
for i in range(len(train_images)):
    if(train_labels[i] in allow):
        train_images_nice.append(train_images[i])
        train_labels_nice.append(allow.index(train_labels[i]))
for i in range(len(test_images)):
    if(test_labels[i] in allow):
        test_images_nice.append(test_images[i])
        test_labels_nice.append(allow.index(test_labels[i]))
test_labels_nice = np.array(test_labels_nice)
test_images_nice = np.array(test_images_nice)
train_labels_nice = np.array(train_labels_nice)
train_images_nice = np.array(train_images_nice)

model = models.Sequential()
model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation = 'relu'))
model.add(layers.Dense(8, activation= 'softmax'))
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])
model.fit(train_images_nice, train_labels_nice, 
          epochs=8, validation_data=(test_images_nice, test_labels_nice))

loss, accuracy = model.evaluate(test_images_nice, test_labels_nice)
print(f"Loss: {loss}")
print(f"Accuracy: {accuracy}")

model.save('image_classifier_nice.model')
