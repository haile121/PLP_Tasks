import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# Data Preparation
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)


train_generator = train_datagen.flow_from_directory(
'dataset/',
target_size=(64, 64),
batch_size=32,
class_mode='categorical',
subset='training'
)


validation_generator = train_datagen.flow_from_directory(
'dataset/',
target_size=(64, 64),
batch_size=32,
class_mode='categorical',
subset='validation'
)


# Model Definition
model = Sequential([
Conv2D(16, (3,3), activation='relu', input_shape=(64,64,3)),
MaxPooling2D(2,2),
Conv2D(32, (3,3), activation='relu'),
MaxPooling2D(2,2),
Flatten(),
Dense(64, activation='relu'),
Dense(train_generator.num_classes, activation='softmax')
])


# Compile Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


# Train Model
history = model.fit(
train_generator,
validation_data=validation_generator,
epochs=5
)


# Save Keras Model
model.save('edge_model.h5')


# Convert to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()


# Save TFLite Model
with open('edge_model.tflite', 'wb') as f:
f.write(tflite_model)


print("TensorFlow Lite model saved successfully.")
