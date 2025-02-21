# Day 20. 100 Days of Data Science Challenge - 02/20/2025

# 🖼️ Binary Image Classification with PyTorch

## 🔍 Project Overview  

In this project, I explored **Deep Learning** using **ResNet18** in **PyTorch** to classify images into two categories:  

✅ **Sloths** 🦥  
✅ **Pain au Chocolat** 🥐  

Instead of training a deep neural network from scratch, I **fine-tuned a pre-trained model** (ResNet18) to recognize our specific classes. This significantly reduces the training time while achieving **high accuracy** by leveraging pre-learned features from ImageNet.  

**🎯 Key Objectives:**  
✔ Understand **feature extraction vs. fine-tuning** in Transfer Learning  
✔ Implement **image preprocessing & augmentation** for robust classification  
✔ Train a **deep learning model using PyTorch**  
✔ Optimize performance using **learning rate scheduling & momentum-based optimizers**  
✔ Evaluate the model using **accuracy metrics & visualization techniques**  

---

## 🗂 Dataset & Preprocessing  

The dataset consists of **two categories (sloths & pain au chocolat)** and is structured into **training & validation sets** as follows:  

Before training, images undergo **multiple preprocessing steps**:  

🔹 **Resizing & Normalization** – Images are resized to **224×224 pixels** and normalized to match ResNet18’s input requirements.  
🔹 **Data Augmentation** – Applied **random cropping, flipping, and normalization** to prevent overfitting and improve generalization.  

---
## 🏗 Model Architecture & Training  

This project utilizes **ResNet18**, a deep convolutional neural network pre-trained on **ImageNet**. The **final fully connected (FC) layer** is modified to classify images into **two categories** (sloths or pain au chocolat).  

### 🔹 Transfer Learning Approach  

✔ **Feature Extraction** – Freeze early layers and train only the final layer.  
✔ **Fine-Tuning** – Unfreeze select layers and optimize for domain-specific classification.  

### 🔹 Training Configuration  

| Parameter            | Value                     |
|----------------------|--------------------------|
| **Model**           | ResNet18 (pre-trained)    |
| **Loss Function**   | CrossEntropyLoss          |
| **Optimizer**       | SGD with momentum         |
| **Learning Rate**   | 0.001 (decayed every 7 epochs) |
| **Batch Size**      | 4                          |
| **Epochs**         | 25                         |

To optimize the learning process, **StepLR learning rate scheduling** is applied to adjust the learning rate dynamically.  

---

## 📊 Model Performance  

**🏆 Final Validation Accuracy: 100%**  

| Epoch | Train Accuracy | Validation Accuracy |
|-------|---------------|---------------------|
| 1     | 87.43%        | 97.73%              |
| 5     | 91.02%        | 100.00%             |
| 10    | 95.81%        | 100.00%             |
| 15    | 94.61%        | 100.00%             |
| 20    | 95.21%        | 100.00%             |
| 25    | 96.41%        | 100.00%             |

💡 **Observations:**  
✔ **Transfer Learning significantly reduced training time** while maintaining high accuracy.  
✔ **Augmentation improved model robustness**, preventing overfitting.  
✔ **Using a learning rate scheduler** helped in better model convergence.  

---

## 🎨 Model Predictions & Visualizations  

After training, the model is evaluated by visualizing **classified images** from the validation set. The predictions are displayed alongside ground truth labels to assess model performance.  

🔹 **Correct Predictions:** Model successfully identifies sloths & pastries.  
🔹 **Edge Cases:** Some misclassifications occur in images with **similar textures or backgrounds**.  

---

## 🏆 Key Takeaways  

✔ **Transfer Learning enables high accuracy with minimal training**  
✔ **Fine-tuning the final layer** was enough for effective classification  
✔ **Data augmentation** significantly improves model robustness  
✔ **Using SGD with momentum & learning rate scheduling** optimizes training  
✔ **Model generalizes well**, achieving **100% validation accuracy**  

