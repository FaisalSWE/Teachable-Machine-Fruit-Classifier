# Fruit Classifier Using Teachable Machine

This project is an image classification tool trained using Google’s Teachable Machine to recognize two classes: **Banana** and **Strawberry**.

## How It Works

- Model trained using Teachable Machine.
- Exported in TensorFlow → Keras format.
- Predicts class using a Python script with TensorFlow.

## Files Included

- `main.py`: Python script to load the model and make predictions.
- `keras_model.h5`: Trained model.
- `labels.txt`: Text file listing class labels .
- `test_image.jpg`: Example image for testing.
- `Screenshot 2025-07-02 193601.png`: Screenshot showing successful prediction.

## 🛠How to Use

1. **Install dependencies** (Python 3.7–3.11):

   ```bash
   pip install tensorflow==2.12.1 pillow numpy
   python main.py
Prediction: Strawberry (99.99% confidence)

