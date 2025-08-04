import streamlit as st
import numpy as np
import pickle
import cv2
from PIL import Image
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image as keras_image

# Load SVM model
with open("svm_model.pkl", "rb") as f:
    svm_model = pickle.load(f)

# Load MobileNetV2 for feature extraction
cnn_model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

st.title("🐾 Cat vs Dog Classifier (SVM + MobileNetV2)")
st.markdown("Upload an image of a **Cat** or **Dog** to classify.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Preprocess image
    img = img.resize((160, 160))
    img_array = keras_image.img_to_array(img)
    img_array = preprocess_input(img_array)
    features = cnn_model.predict(np.expand_dims(img_array, axis=0), verbose=0)
    features_flat = features.flatten().reshape(1, -1)

    # Predict
    prediction = svm_model.predict(features_flat)[0]
    confidence = svm_model.predict_proba(features_flat)[0][prediction]

    label = "🐱 Cat" if prediction == 0 else "🐶 Dog"
    st.success(f"Prediction: **{label}** with {confidence * 100:.2f}% confidence.")
