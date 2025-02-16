# Day 15. 100 Days of Data Science Challenge - 02/15/2025

# 🌱 BeanSight – Uncovering Bean Disease Patterns with PCA  


## 📝 Project Overview  
**BeanSight** explores plant pathology using **Principal Component Analysis (PCA)** to analyze bean leaf disease images. The goal is to **reduce high-dimensional image data** while preserving 95% of the variance, then reconstruct and compare the images.  

🛠 **Key Techniques:**  
✔️ Image Preprocessing (Grayscale Conversion, Resizing, Flattening)  
✔️ Data Standardization (Mean = 0, Unit Variance)  
✔️ Principal Component Analysis (PCA) for Dimensionality Reduction  
✔️ Image Reconstruction & Visualization  

---

## 🌿 Dataset: Bean Disease Dataset  
📌 **Source:** [Kaggle – Bean Disease Dataset](https://www.kaggle.com/datasets/therealoise/bean-disease-dataset)  
📍 **Captured in bean fields** by Makerere AI Lab in collaboration with Uganda’s **National Crops Resources Research Institute (NaCRRI)**.  

### **Classes in the Dataset**  
🍃 **Healthy** – Normal bean leaves  
🍂 **Angular Leaf Spot** – Fungal disease causing brown lesions  
🌾 **Bean Rust** – Rust-colored spores affecting the leaves  

The dataset contains **color images** of bean leaves, which are preprocessed for PCA-based analysis.  

---

## 🛠 Objectives & Methodology  

### 🔹 **1. Data Preprocessing**  
📌 Convert images to **grayscale** (removing RGB channels).  
📌 Resize images to **64×64 pixels** for consistency.  
📌 Flatten images into **1D arrays (4096 features each)** for PCA.  
📌 Store images and labels in NumPy arrays for efficient computation.  

### 🔹 **2. Data Standardization**  
📌 Compute **mean & standard deviation** for normalization.  
📌 Scale data to have **zero mean & unit variance** (crucial for PCA).  

### 🔹 **3. Principal Component Analysis (PCA)**  
📌 **Goal:** Reduce dimensionality while retaining **95% of variance**.  
📌 **Outcome:** PCA determined that **595 components** were sufficient.  
📌 **Why?** Fewer dimensions mean faster processing and better efficiency! 🚀  

### 🔹 **4. Image Reconstruction & Visualization**  
📌 **Reconstruct images** using PCA-transformed data.  
📌 Compare **original vs. reconstructed images** to evaluate PCA’s effectiveness.  
📌 Display side-by-side results for **qualitative analysis**.  

---

## 📊 Key Insights & Learnings  

✔️ **Dimensionality Reduction Works!** PCA compresses images while keeping important visual patterns.  
✔️ **Reconstructed images closely resemble originals**, proving PCA’s ability to retain essential features.  
✔️ **High-dimensional image data can be represented efficiently** with far fewer components.  
✔️ This technique is useful for **disease classification, anomaly detection, and deep learning preprocessing**.  

---

## 📌 Future Improvements  

🔹 **Combine PCA with ML models** (e.g., Random Forests, SVM, CNNs) for disease classification.  
🔹 **Experiment with different variance thresholds** (e.g., 90% vs. 99%) to see impact on image quality.  
🔹 **Introduce Data Augmentation** to improve generalization in disease classification tasks.  

---

## 💡 Reflections  

This project was an exciting **deep dive into PCA** and its potential for real-world applications in **agriculture and disease detection**. **Reducing dimensions while retaining crucial patterns** is a powerful tool that can be applied in many fields, from medical imaging to AI-driven farming.  

🌱 **Next Steps:** I plan to extend this project by **combining PCA with deep learning** for automatic disease classification!  

---

## 👤 About Me  
👋 Hey, I'm [Your Name]! I'm currently on a **100 Days of Data Science** journey, and this is my **Day 15 Project**.  
Follow my progress and let's connect! 🚀  

📌 **GitHub:** [github.com/yourusername](https://github.com/yourusername)  
📌 **Twitter:** [twitter.com/yourhandle](https://twitter.com/yourhandle)  

---

## 📜 License  
MIT License – Feel free to use and modify!  

