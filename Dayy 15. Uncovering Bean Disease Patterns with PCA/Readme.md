# Day 15. 100 Days of Data Science Challenge - 02/15/2025

# 🌿 BeanVision – Uncovering Bean Diseases with PCA

## 📝 Project Overview  
Plants are the backbone of agriculture, but diseases can threaten their health and yield. In **BeanVision**, I leverage **machine learning and dimensionality reduction** to analyze and classify bean leaf diseases. This project explores the **Bean Disease Dataset** using **Principal Component Analysis (PCA), clustering techniques, and neural networks** to uncover patterns in bean leaf images.  

🛠 **Techniques Used:**  
✔️ Image Processing (Grayscale Conversion, Resizing, Flattening)  
✔️ **Dimensionality Reduction** – PCA, t-SNE, LLE, and MDS  
✔️ **Clustering** – K-Means & Expectation-Maximization (GMM)  
✔️ **Deep Learning** – Feedforward Neural Network for Classification  
✔️ **Visualizations** – Image Reconstructions & Cluster Scatter Plots  

---

## 🌿 Dataset: Bean Disease Dataset  
📌 **Source:** [Kaggle – Bean Disease Dataset](https://www.kaggle.com/datasets/therealoise/bean-disease-dataset)  
📍 Captured in **bean fields** by Makerere AI Lab in collaboration with Uganda’s **National Crops Resources Research Institute (NaCRRI)**.  

### **Classes in the Dataset**  
🍃 **Healthy** – Normal bean leaves  
🍂 **Angular Leaf Spot** – Fungal disease causing brown lesions  
🌾 **Bean Rust** – Rust-colored spores affecting the leaves  

The dataset consists of **grayscale images** that undergo preprocessing for further analysis.  

---

## 🛠 Objectives & Methodology  

### 🔹 **1. Data Preprocessing**  
📌 Convert images to **grayscale** (removing RGB channels).  
📌 Resize images to **64×64 pixels** for uniformity.  
📌 Flatten images into **1D vectors** (4096 features each).  
📌 Store processed images in **NumPy arrays** for efficient computation.  

### 🔹 **2. Principal Component Analysis (PCA)**  
📌 **Goal:** Reduce dimensionality while preserving **95% of variance**.  
📌 **Outcome:** PCA determined that **595 components** were sufficient.  
📌 **Visualization:** Original vs. Reconstructed Images to evaluate PCA’s effectiveness.  

### 🔹 **3. Clustering for Pattern Recognition**  
📌 **K-Means Clustering** – Optimal **k=3** (Silhouette Score & Elbow Method).  
📌 **Expectation-Maximization (Gaussian Mixture Model)** – Optimal clusters identified using **BIC & AIC criteria**.  
📌 **Scatter plots with PCA, t-SNE, LLE, and MDS** to visualize feature separability.  

### 🔹 **4. Neural Network for Disease Classification**  
📌 **Deep Learning Model** – A feedforward **neural network (DNN)** trained to classify bean leaves.  
📌 **Architecture:**  
   - Dense layers with **ReLU activation**  
   - Batch normalization for stable learning  
   - Output layer: **Softmax activation** for multi-class classification
     
📌 **Training Observations:**  
   - Model **successfully classified bean diseases** with improved accuracy over time.  
   - Validation loss fluctuated, hinting at slight **overfitting**.  

---

## 📊 Key Insights & Learnings  

✔️ **PCA significantly reduced image dimensions** while preserving important features.  
✔️ **t-SNE and LLE provided clearer cluster separations** than MDS.  
✔️ **K-Means (k=3) best represented the disease clusters**, aligning with known classes.  
✔️ **Neural Network classification performed well** but required careful tuning to prevent overfitting.  
✔️ **Future Improvements:** Combining PCA with CNNs for better disease classification accuracy.  

---

## 📌 Future Enhancements  

🔹 **Try advanced dimensionality reduction techniques** (e.g., UMAP, Autoencoders).  
🔹 **Experiment with CNNs** for feature extraction and classification.  
🔹 **Augment dataset** with synthetic samples to improve model generalization.  
🔹 **Combine clustering & classification** for a hybrid disease detection system.  

---

## 💡 Reflections  

This project reinforced **the power of dimensionality reduction** and **clustering techniques** in **image analysis**. It demonstrated that even with **simpler models like PCA & K-Means**, we can **effectively uncover patterns** in complex datasets. The **neural network approach** added another layer of validation to the insights gained from unsupervised learning.  
