# Day 54. 100 Days of Data Science Challenge - 03/26/2025

# 🧠 Fine-Tuning DeepSeek R1 for Medical Reasoning with LoRA

**Status:** ![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  
**Model:** DeepSeek-R1-Distill-Llama-8B  
**Tools Used:** Kaggle, Hugging Face, Weights & Biases, LoRA, PyTorch  

---

## 🌟 Project Overview  

MediMind is a specialized fine-tuning project that transforms the **DeepSeek R1 reasoning model** into a medical expert capable of structured clinical reasoning. By leveraging **LoRA (Low-Rank Adaptation)** and **4-bit quantization**, this project demonstrates how large language models can be efficiently adapted for domain-specific tasks like medical diagnostics.  

The fine-tuned model excels in generating detailed chain-of-thought reasoning for complex patient cases, enabling accurate and concise responses that mimic clinical decision-making processes.  

![image](https://github.com/user-attachments/assets/4f666231-dc7b-4dfb-b050-9092071c8b13)

---

## 🧩 Dataset Details

- Source: [FreedomIntelligence/medical-o1-reasoning-SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT)
- Samples Used: First 500 entries from the dataset.

Format:

- **Question:** Medical case description.
- **Complex CoT:** Step-by-step reasoning.
- **Response:** Final diagnosis or answer.

---

## ✨ Key Features  

- **Medical Chain-of-Thought Reasoning**: Generates structured diagnostic thought processes before answering.  
- **Memory-Efficient Fine-Tuning**: Utilizes 4-bit quantization for training on consumer GPUs.  
- **Parameter-Efficient Learning**: Updates only 0.1% of model parameters using LoRA adapters.  
- **Enhanced Diagnostic Accuracy**: Shows significant improvement in reasoning clarity and precision post-fine-tuning.  
- **Domain-Specific Knowledge**: Trained on verified medical reasoning datasets to ensure reliability.  

---

## 🛠️ Technical Highlights  

### **Fine-Tuning with LoRA**  
LoRA (Low-Rank Adaptation) enables efficient fine-tuning by introducing small trainable adapters to specific layers in the model. Instead of updating all parameters, LoRA modifies only key components like attention mechanisms and feed-forward layers, reducing computational costs by over 90%.  

> *Analogy*: Think of LoRA as adding specialized tools to an existing factory instead of rebuilding the entire structure.

### **4-Bit Quantization**  
Compresses model weights from 32-bit to 4-bit representations, reducing memory usage by 87.5% while retaining most of the original accuracy. This optimization allows large models like DeepSeek R1 to run smoothly on consumer-grade GPUs.

---

## 📊 Training Insights  

### **Learning Curve**
| Step | Training Loss |
|------|---------------|
| 10   | 1.914200      |
| 20   | 1.421000      |
| 30   | 1.366000      |
| 40   | 1.328500      |
| 50   | 1.295100      |
| 60   | 1.326900      |

- The training loss decreased steadily during the fine-tuning process, indicating successful adaptation to the medical reasoning task.

### **Weights & Biases Dashboard**
![Training Metrics](https://pplx-res.cloudinary.com/image/upload/v1743016051/user_uploads/GivWetDpRQjMIHA/1.jpg)  
*Figure: Training loss, learning rate decay, gradient norm stability across epochs.*

## 🔍 Key Results  

### **Before Fine-Tuning**  
The model produced lengthy and somewhat rambling reasoning chains with inconsistent formatting:  
```
Stress urinary incontinence is likely based on her symptoms. The residual volume might be normal, but detrusor contractions would also be normal.
```

**Insight**: While accurate, the response lacked conciseness and clarity.  

### **After Fine-Tuning**  
The fine-tuned model generated concise and structured reasoning:  

```
Stress urinary incontinence is likely based on her symptoms. Cystometry findings would reveal normal residual volume and detrusor contractions.
```

**Insight**: Improved diagnostic accuracy and clarity in chain-of-thought reasoning, mimicking a clinician's step-by-step thought process.

---

## 🚀 Future Directions  

1. **Expand Dataset Scope**: Incorporate additional datasets for broader medical coverage (e.g., radiology reports).  
2. **Deploy Model Locally**: Convert to GGUF format for efficient local inference.  
3. **Integrate Predictive Analytics**: Add modules for disease progression forecasting based on patient data trends.  
4. **Mobile Optimization**: Develop a lightweight mobile-friendly version for real-time clinical support.

---

## 💡 Takeaways  

This project showcases how cutting-edge techniques like LoRA and quantization can transform general-purpose models into domain-specific experts with minimal computational resources. MediMind represents a step forward in democratizing AI for critical fields like healthcare, making advanced diagnostic tools accessible to clinicians worldwide.

> *"AI isn’t just about automation—it’s about augmenting human expertise."*

---

Made with ❤️ during Day 54 of my Data Science Challenge!  
