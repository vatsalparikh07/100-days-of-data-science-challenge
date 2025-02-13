# Day 13. 100 Days of Data Science Challenge - 02/13/2025

# 🧠 BERT Text Classification
**Fine-tuning BERT for binary classification of food vs sports articles**

## 🚀 Project Overview
This project fine-tunes a pre-trained BERT model to classify text as either food-related or sports-related. Key highlights:

- Achieved **97.5% accuracy** on test set
- Processed **200 web-scraped articles** (100 food, 100 sports)
- Implemented custom dataset and data loading pipeline
- Fine-tuned BERT using Hugging Face Transformers library

## 📊 Dataset 
- **Source**: Web-scraped articles from food and sports websites
- **Size**: 200 articles total (160 train, 40 test)
- **Classes**: Food (0), Sports (1)
- **Preprocessing**: BERT tokenization, padding, truncation

## 🛠️ Implementation Details
- Model: `bert-base-uncased` from Hugging Face
- Optimizer: AdamW (learning rate: 1e-5)
- Training: 3 epochs, batch size of 4
- Hardware: GPU-enabled (CUDA)

## 📈 Results
- Test Accuracy: 97.5%
- Training Time: ~52 minutes (3 epochs)

## 🔍 Key Findings
1. BERT outperformed traditional ML models significantly
2. Small dataset (200 examples) was sufficient for high accuracy
3. Domain-specific fine-tuning highly effective for binary classification

## 🌟 Future Improvements
- Experiment with other pre-trained models (RoBERTa, DistilBERT)
- Implement cross-validation for more robust evaluation
- Explore multi-class classification with more categories
