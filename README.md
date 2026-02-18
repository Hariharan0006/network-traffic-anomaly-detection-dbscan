# 🚨 Network Traffic Anomaly Detection System using DBSCAN
![Recommendation Result](sample_1.png)
## 📌 Project Overview
Modern networks generate massive volumes of traffic, making it difficult for traditional rule-based intrusion detection systems to identify unknown or evolving cyber attacks.  
This project implements an **unsupervised anomaly detection system** using **DBSCAN** to detect abnormal network behavior without relying on predefined labels.

---

## 🧠 Business Problem
Rule-based security systems fail to detect zero-day and unknown attacks due to static rules. Security analysts require a data-driven approach that can automatically identify suspicious patterns in real time.

---

## 🎯 Business Objective
- Detect abnormal network traffic
- Identify potential intrusions or cyber attacks
- Reduce manual monitoring effort
- Improve security response time

---

## 📊 Dataset
- **UNSW-NB15 Network Intrusion Dataset**
- Source: Kaggle / UNSW Official
- Subset used: 50,000 records (optimized for DBSCAN)

---

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn (DBSCAN, PCA)
- Flask (Web Application)
- Matplotlib & Seaborn
- MySQL (Data Storage)
- HTML, CSS (UI)

---

## ⚙️ Project Architecture


---

## 🔍 Feature Selection
Selected key network behavior features:
- `dur`, `spkts`, `dpkts`
- `rate`, `dload`, `sinpkt`

Highly correlated features were removed to avoid distance bias in DBSCAN.

---

## 📈 Model & Evaluation
- **Algorithm:** DBSCAN (Density-Based Clustering)
- **Why DBSCAN?**
  - No need to predefine number of clusters
  - Effectively identifies noise/anomalies
  - Suitable for cybersecurity data

### Validation:
- Post-hoc evaluation using known attack labels
- Majority of detected anomalies correspond to real attacks
- Silhouette score computed on non-noise clusters

---

## 🌐 Web Application
- Upload test CSV file
- Detect anomalies in real time
- Visualize results using PCA plots
- Display total anomalies detected

---

## ✅ Results
- Successfully detected multiple attack categories:
  - DoS
  - Exploits
  - Fuzzers
  - Worms
  - Backdoors
- Clear separation between normal and anomalous traffic

---

## 🚀 How to Run
```bash
pip install -r requirements.txt
python train_model.py
python app.py

http://127.0.0.1:5000


---
