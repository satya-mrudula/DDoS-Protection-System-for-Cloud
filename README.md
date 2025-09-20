# Intelligent DDoS Protection System with ML & Real-time Mitigation 🚀

![DDoS Protection](assets/demo.gif) <!-- Optional: add a GIF of your traffic/blocking demo -->

---

## 🔹 Introduction

This project combines **Machine Learning-based anomaly detection** with **rule-based mitigation** to prevent DDoS attacks in real-time.  
Designed for **live demonstration on any laptop**, it simulates both normal and attack traffic while showcasing intelligent IP blocking.

---

## 🔹 Features

- **Real-time traffic analysis** with ML and rule-based logic  
- **Attack detection using Isolation Forest**  
- **Automatic IP blocking and logging**  
- **Minimal setup**: runs locally with just Python  
- **Extensible**: easy to integrate into real networks  

---

## 🔹 Repository Structure


DDoS-Protection-System/
│
├── backend/ # Backend server & traffic simulation
│ ├── app.py
│ ├── detector.py
│ ├── mitigation.py
│ └── traffic_generator.py
│
├── models/ # Pre-trained ML model
│ └── ddos_model.pkl
│
├── notebooks/ # Optional: ML workflow, visualizations
│ └── model_training.ipynb
│
├── assets/ # Demo GIFs / screenshots
├── requirements.txt
├── README.md
└── LICENSE

---

## 🔹 Installation
#bash
# Clone repo
git clone <your_repo_url>
cd DDoS-Protection-System

# Create virtual environment
python -m venv ddos-env
ddos-env\Scripts\activate    # Windows
# OR
source ddos-env/bin/activate # Linux/Mac

# Install dependencies
pip install -r requirements.txt
