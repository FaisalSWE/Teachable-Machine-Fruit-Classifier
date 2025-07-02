# Fruit Classifier (Banana or Strawberry)

This is a simple fruit image classifier trained with **Google Teachable Machine**. It can predict whether an image shows a **banana** or a **strawberry**.

---

## What This Project Does

- Uses a Keras model (`keras_model.h5`) exported from Teachable Machine.
- Classifies images into two categories: Banana or Strawberry.
- Runs in Python using TensorFlow.

---

## Files Included

| File                               | Purpose                                  |
|------------------------------------|------------------------------------------|
| `main.py`                          | Python script to run prediction          |
| `keras_model.h5`                   | Trained  model                           |
| `labels.txt`                       | List of the two classes names            |
| `Screenshot 2025-07-02 193601.png` | Screenshot of script output              |

---

##  How to Use This Project

### Requirements

- Python **3.7 to 3.11**
- Install dependencies:

```bash
pip install tensorflow==2.12.1
