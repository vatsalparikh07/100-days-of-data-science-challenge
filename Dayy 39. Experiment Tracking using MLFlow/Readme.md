# Day 39. 100 Days of Data Science Challenge - 03/11/2025

## 🚀 MLflow Experiment Tracking – [DagsHub Repository](https://dagshub.com/vatsalparikh07/mario_vs_wario)

## 🌟 Project Overview  

Machine learning models don’t exist in isolation—they evolve through **constant experimentation, hyperparameter tuning, and iterative improvements**. But how do you keep track of all these experiments?  

Enter **MLflow**—an open-source platform that brings order to chaos by enabling **live experiment tracking, model registry, and seamless deployment**.  

In this project, I integrated **MLflow with DagsHub**, setting up a **fully remote tracking server** to log parameters, metrics, and artifacts—ensuring complete reproducibility and collaboration in ML projects.  

🚀 **Key Highlights:**  
✔️ Set up a **remote MLflow Tracking Server** with DagsHub  
✔️ Implemented **live logging of ML experiments**  
✔️ Tracked **hyperparameters, performance metrics, and artifacts**  
✔️ Automated **model versioning and experiment comparison**  

---

## 🎯 Why Does This Matter?  

📌 **Reproducibility is a Nightmare Without Experiment Tracking**  
- Have you ever lost track of **which model version had the best accuracy**?  
- Have you ever struggled to **replicate an experiment after months**?  

**MLflow solves this!** It provides an easy way to:  
✅ **Log every run** – No more guessing what parameters worked best  
✅ **Compare experiments** – Quickly identify improvements over past models  
✅ **Deploy seamlessly** – Register models for production use  

This project takes **machine learning from “just code” to a structured, scalable, and trackable process**.  

---

## 📂 Data Collection & Setup  

🔹 **Dataset:** Trained a deep learning model for **image classification (Mario vs. Wario Dataset)**  
🔹 **Experimentation Environment:** Google Colab & DagsHub  
🔹 **Tracking Setup:** Used **MLflow with remote logging**  

---

## 🛠 Analytical Approach  

### 1️⃣ **Experiment Tracking with MLflow**  
- Logged **hyperparameters**, **model metrics**, and **artifacts** for every experiment  
- Stored results **remotely** on DagsHub, enabling **team collaboration**  

### 2️⃣ **Automated Model Versioning**  
- Each **trained model was automatically versioned** in MLflow  
- Tracked **which experiment performed best** for future deployment  

### 3️⃣ **Hyperparameter Tuning**  
- Tracked how **learning rate, batch size, and epochs** influenced performance  
- Compared runs to find **optimal configurations**  

### 4️⃣ **Seamless Deployment Integration**  
- **MLflow Model Registry** stored the best-performing model  
- Enabled **quick deployment to AWS** or local servers  

---

## 🔥 Key Insights & Findings  

| **Experiment ID**  | **Accuracy** | **Loss** | **Hyperparameters**            |  
|--------------------|-------------|----------|--------------------------------|  
| `exp_001`         | 67.3%       | 0.64     | LR = 0.001, Epochs = 5         |  
| `exp_002`         | 58.2%       | 0.69     | LR = 0.0005, Epochs = 10       |  
| `exp_003`         | 72.8%       | 0.59     | LR = 0.0008, Epochs = 7        |  

### ✨ Observations  

- **Experiment 003 performed best** with **72.8% accuracy**  
- Increasing **epochs beyond 7 led to overfitting**  
- Learning rate **0.0008 provided optimal convergence**  

---

## 🎨 MLflow Dashboard Highlights  

✅ **Interactive UI for Experiment Tracking** – View and compare past runs  
✅ **Live Metric Logging** – Track loss, accuracy, and validation scores in real-time  
✅ **Model Registry & Versioning** – Store, retrieve, and deploy the best models  

🚀 **[View Experiment Logs](https://dagshub.com/vatsalparikh07/mario_vs_wario/experiments)**  

---

## 🚧 Challenges & Solutions  

### Challenge: **Tracking ML Experiments Across Multiple Runs**  
✅ **Solution:** Used **MLflow Tracking Server** to automatically log and retrieve experiment history  

### Challenge: **Choosing the Best Model Version**  
✅ **Solution:** Implemented **automated model comparison** using MLflow’s experiment dashboard  

### Challenge: **Remote Storage for Artifacts**  
✅ **Solution:** Used **DagsHub integration** to store artifacts and logs in a **centralized cloud repository**  

---

## 💡 Future Enhancements  

🔹 **Hyperparameter Optimization** – Use **Optuna or Bayesian Optimization** to find the best parameters automatically  
🔹 **Real-time Monitoring** – Set up **Grafana dashboards** for live performance tracking  
🔹 **Deployment Pipeline** – Automate model deployment using **CI/CD with MLflow Models**  

---


### ✨ Final Thoughts  

This project bridges the gap between **machine learning and MLOps**, making experiments **traceable, reproducible, and scalable**. **MLflow is not just a tool—it’s a necessity for every serious data scientist.**  
💬 **Let’s discuss!** If you’re passionate about **ML experiment tracking, automation, or MLOps**, let’s connect and exchange ideas! 😊  
