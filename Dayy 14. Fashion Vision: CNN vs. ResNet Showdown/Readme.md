# Day 14. 100 Days of Data Science Challenge - 02/14/2025

# 👕 Fashion Vision: CNN vs. ResNet Showdown  

Deep learning and fashion—what’s not to love? For today’s challenge, I built an **image classification model** that can recognize different types of clothing. The dataset includes:  
👟 **Shoes** | 👚 **T-Shirts** | 👖 **Bottoms**  

To solve this classification problem, I tested **two different approaches**:  
1️⃣ **Fine-tuning a Pretrained ResNet50 Model**  
2️⃣ **Building a Convolutional Neural Network (CNN) from Scratch**  

Which one is better? Let’s find out! 🚀  

---

## 🗂 The Dataset  
This dataset consists of **300 images (100 per class)** collected and organized into folders.  
To ensure proper training, the dataset was split into:  
- **Training Set (64%)** – The model learns from this.  
- **Validation Set (16%)** – Used to tune hyperparameters.  
- **Test Set (20%)** – Final evaluation to measure performance.  

### 🔹 Preprocessing & Data Augmentation  
Before feeding images into the models, I applied **preprocessing and augmentation** to improve generalization:  
✔️ **Resizing** all images to **224 × 224 pixels**.  
✔️ **Normalizing** pixel values to the `[0,1]` range.  
✔️ **Data Augmentation** (only for training data):  
   - **Random Rotation**  
   - **Shifting & Shearing**  
   - **Zooming & Flipping**  

These techniques helped **prevent overfitting** and ensured that the model learned robust patterns!  

---

## 🛠 The Models  

### 🔹 **1. Transfer Learning: ResNet50**  
**Why ResNet50?** It’s a powerful, pretrained convolutional neural network that has already learned high-level image features from millions of images.  
Here’s how I adapted it for this task:  
- Used a **pretrained ResNet50 model** as a feature extractor.  
- **Removed the top layers** and added a custom classification head.  
- **Froze the base layers** to retain pretrained knowledge.  
- **Used Adam optimizer** with **categorical crossentropy loss**.  

💡 **Results:** The model trained quickly but had a **test accuracy of ~61.67%**. Not bad, but I wanted to see if I could do better!  

---

### 🔹 **2. Custom CNN (From Scratch)**  
I designed and trained a **Convolutional Neural Network (CNN) from scratch**.  
Here’s the architecture:  
1️⃣ **Conv2D Layer (32 filters, 3×3 kernel)** – Extracts low-level patterns.  
2️⃣ **MaxPooling Layer** – Reduces spatial dimensions.  
3️⃣ **Conv2D Layer (64 filters, 3×3 kernel)** – Captures more complex features.  
4️⃣ **MaxPooling Layer** – Further reduces size.  
5️⃣ **Flatten Layer** – Converts feature maps into a 1D vector.  
6️⃣ **Dense Layer (512 neurons, ReLU activation)** – Fully connected for learning.  
7️⃣ **Dense Layer (3 neurons, Softmax activation)** – Outputs class probabilities.  

💡 **Results:** **This model performed better than ResNet50!**  
Although training took longer, it generalized well and achieved higher accuracy.  

---

## 📊 Results & Key Takeaways  
Here’s what I learned from comparing both models:  
📌 **CNN (Trained from Scratch) > ResNet50 in test accuracy.**  
📌 **Transfer learning is fast but requires fine-tuning.**  
📌 **More data = Better CNN performance.**  
📌 **Data augmentation helped the CNN generalize better.**  
📌 **Pretrained models may not always be the best solution!**  

I also visualized **correct vs. incorrect predictions** to analyze where the models struggled.  

---

## 📉 Training Performance  
### 🔹 **Loss & Accuracy Plots**  
I plotted **training vs. validation loss and accuracy** to understand model performance.  

- **Loss Observation:**  
  - The CNN model showed a **steady decrease in training loss**, while the validation loss fluctuated slightly before stabilizing.  
  - ResNet50 initially performed well but plateaued early.  

- **Accuracy Observation:**  
  - The CNN model improved steadily and **outperformed ResNet50 on the test set**.  
  - ResNet50 started strong but struggled to generalize.  

---

## 🚀 What’s Next?  
🔹 **Try deeper CNN architectures** to push accuracy even further.  
🔹 **Experiment with other pretrained models** (EfficientNet, MobileNet).  
🔹 **Fine-tune ResNet50 more aggressively** (adjust learning rates, unfreeze more layers).  
🔹 **Collect more data** to enhance model robustness.  

---

## 💡 Reflections
Day 14 of 100 Days of Data Science was an eye-opener!

🔹Custom models can sometimes outperform pretrained ones!

🔹Preprocessing & augmentation are critical for good performance.

🔹Experimenting with different architectures is key to deep learning success.

This was an exciting project, and I can’t wait to explore more deep learning challenges! 🚀
