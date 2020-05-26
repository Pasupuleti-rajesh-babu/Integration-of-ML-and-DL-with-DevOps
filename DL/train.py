import pandas as pd
from keras.optimizers import Adam
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('/mnt/wines.csv')

y = dataset['Class']

y_cat = pd.get_dummies(y)

x = dataset.drop('Class', axis=1)

x_train, x_test, y_train, y_test = train_test_split(x,y_cat,test_size=0.1,random_state=20)

model = Sequential()

model.add(Dense(units=64, input_shape=(13,), activation='relu'))
model.add(Dense(units=32, activation="relu"))
model.add(Dense(units=16, activation="relu"))
model.add(Dense(units=3, activation='softmax'))

model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=Adam())

model.fit(x_train,y_train, validation_data=(x_test,y_test), epochs=20, verbose=0)

accuracy = model.evaluate(x_test, y_test, verbose=0)
accuracy = accuracy[1]*100
print(accuracy)

import os
os.system("touch /mnt/accuracy.txt")
os.system("echo {} > /mnt/accuracy.txt".format(accuracy))

model.save('/mnt/multiclassNN.h5')



