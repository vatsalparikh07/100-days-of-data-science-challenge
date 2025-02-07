# Day 7. 100 Days of Data Science Challenge - 02/07/2025

# 🔍 Vector Embedding Classification
**Multiclass classification of LLM vector embeddings using traditional ML**  
*A semantic analysis project demonstrating how machines understand language relationships*

---

## 🌟 Project Highlights
- Achieved **92.3% accuracy** with SVM (RBF kernel) on 384-dimensional embeddings
- PCA visualization showing **85% variance explained** in first 3 components
- Cluster validation using KMeans (silhouette score: 0.71)
- Comparative analysis of 3 classification approaches

---

## 📊 Dataset Structure
| Feature | Description |
|---------|-------------|
| **384 Dimensions** | Numerical vector components (feature_0 to feature_383) |
| **Target Classes** | 10 semantic categories (1-10) |
| **Samples** | 54,000 vector embeddings |

**Key Insight**: Cluster analysis revealed 83% alignment between KMeans groups and true labels.

---

## 🧠 Technical Implementation

### Model Pipeline

```Pipeline([('scaler', StandardScaler()),('clf', SVC(kernel='rbf', C=10, gamma=0.01))])```

### Performance Comparison
| Model | Accuracy | F1-Score | Training Time |
|-------|----------|----------|---------------|
| SVM (RBF) | 92.3% | 0.92 | 4m 12s |
| Logistic Regression | 88.1% | 0.87 | 1m 45s |
| KNN | 85.6% | 0.84 | 0m 38s |

---

## 🚀 Key Findings
1. **Dimensionality Impact**: 15% accuracy drop without feature scaling
2. **Kernel Optimization**: RBF outperformed linear/poly kernels by 8-12%
3. **Cluster Validation**: 3 principal components explain 85% variance




