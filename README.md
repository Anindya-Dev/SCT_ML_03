# SCT_ML_03
# 🐱🐶 Cat vs Dog Image Classifier using SVM (Streamlit App)

This project demonstrates how to classify images of cats and dogs using a **Support Vector Machine (SVM)** model. The trained model is wrapped in a simple and intuitive **Streamlit UI** for real-time image prediction.

---

## 🚀 Features

- 📦 Pretrained SVM model trained on 20,000+ cat and dog images.
- 🧠 Uses **feature extraction** from images with optional CNN preprocessing.
- 📤 Upload any image of a cat or dog to classify it.
- ✅ Fast and lightweight prediction using `LinearSVC`.

---

## 🗂️ Project Structure

SCT_ML_02/
├── app.py # Main Streamlit application
├── Mall_Customers/ # Folder containing sample dataset
│ └── Mall_Customers.csv
├── requirements.txt # Required Python packages
└── README.md # You're reading it!



▶️ How to Run Locally
Install dependencies:
pip install -r requirements.txt
#Use this command to run the app on a localhost server
streamlit run app.py