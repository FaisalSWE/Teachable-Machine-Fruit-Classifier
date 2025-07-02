import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model('keras_model.h5')

# Load labels
with open('labels.txt', 'r') as f:
    class_names = [line.strip() for line in f.readlines()]

def preprocess_image(image_path):
    img = Image.open(image_path).convert('RGB').resize((224, 224))
    img_array = np.array(img).astype(np.float32)
    normalized_img = (img_array / 127.5) - 1
    return np.expand_dims(normalized_img, axis=0)

image_path = 'image path'  # Replace with your image filename

image = preprocess_image(image_path)
prediction = model.predict(image)
predicted_index = np.argmax(prediction[0])
predicted_class = class_names[predicted_index]
confidence = prediction[0][predicted_index] * 100

print(f'Prediction: {predicted_class} ({confidence:.2f}% confidence)')
