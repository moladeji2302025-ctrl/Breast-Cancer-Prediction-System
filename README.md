# Breast Cancer Prediction System

A machine learning-based web application that predicts whether a breast tumor is benign or malignant using diagnostic measurements.

## 🎯 Project Overview

This project implements a complete machine learning pipeline for breast cancer classification:
- **Model**: Logistic Regression trained on the Breast Cancer Wisconsin (Diagnostic) dataset
- **Features**: 5 carefully selected features from tumor measurements
- **Web Interface**: Flask-based web application for easy predictions
- **Accuracy**: High-performance model with comprehensive evaluation metrics

## 📁 Repository Structure

```
Breast-Cancer-Prediction-System/
├── app.py                              # Flask web application
├── requirements.txt                    # Python dependencies
├── BreastCancer_hosted_webGUI_link.txt # Deployment information
├── model/
│   ├── model_building.ipynb           # Jupyter notebook for model development
│   └── breast_cancer_model.pkl        # Trained model (Joblib format)
├── static/
│   └── style.css                       # Web interface styling
└── templates/
    └── index.html                      # Web interface template
```

## 🚀 Features

### Model Development (Part A)
- ✅ Logistic Regression algorithm
- ✅ 5 selected features: mean radius, mean texture, mean perimeter, mean area, mean smoothness
- ✅ Data preprocessing and feature scaling
- ✅ Model evaluation with accuracy, precision, recall, and F1-score
- ✅ Model persistence using Joblib
- ✅ Demonstration of model reloading and prediction

### Web GUI (Part B)
- ✅ Flask-based web application
- ✅ User-friendly interface for inputting tumor features
- ✅ Real-time prediction display
- ✅ Confidence scores for predictions
- ✅ Responsive design with modern UI/UX

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/moladeji2302025-ctrl/Breast-Cancer-Prediction-System.git
   cd Breast-Cancer-Prediction-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify model file exists**
   ```bash
   ls model/breast_cancer_model.pkl
   ```

## 📊 Running the Application

### Option 1: Web Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to: `http://localhost:5000`
   - Enter the tumor feature values
   - Click "Predict Tumor Type" to get results

### Option 2: Jupyter Notebook

1. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Open the notebook**
   - Navigate to `model/model_building.ipynb`
   - Run all cells to see the complete model development process

## 📈 Model Performance

The Logistic Regression model demonstrates excellent performance on the test set:
- **Accuracy**: ~95-97%
- **Precision**: High precision for both classes
- **Recall**: Balanced recall scores
- **F1-Score**: Strong F1 scores indicating good overall performance

## 🔬 Input Features

The model uses the following 5 features for prediction:

1. **Mean Radius**: Average distance from center to points on the perimeter (typical range: 6-28)
2. **Mean Texture**: Standard deviation of gray-scale values (typical range: 9-40)
3. **Mean Perimeter**: Average size of the core tumor (typical range: 43-188)
4. **Mean Area**: Average area of the tumor (typical range: 143-2500)
5. **Mean Smoothness**: Average local variation in radius lengths (typical range: 0.05-0.16)

## 🎨 Web Interface

The web interface provides:
- Clean, modern design with gradient backgrounds
- Input validation and helpful hints for each feature
- Real-time prediction with confidence scores
- Color-coded results (green for benign, red for malignant)
- Detailed input summary for verification
- Fully responsive design for mobile and desktop

## 🔒 Security & Privacy

- No data is stored or transmitted to external servers
- All predictions are performed locally
- Educational purpose only - not for medical diagnosis

## 📝 Technologies Used

- **Machine Learning**: scikit-learn, pandas, numpy
- **Model Persistence**: Joblib
- **Web Framework**: Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Visualization**: Jupyter Notebook

## 🌐 Deployment

The application can be deployed to various platforms:
- Vercel
- Heroku
- AWS
- Google Cloud Platform
- Azure

Deployment details are available in `BreastCancer_hosted_webGUI_link.txt`

## ⚠️ Disclaimer

This system is developed for **educational purposes only**. It should NOT be used as a substitute for professional medical diagnosis. Always consult qualified healthcare professionals for medical advice and diagnosis.

## 📄 License

This project is open source and available for educational use.

## 👨‍💻 Author

**Name**: [Student Name]  
**Matric Number**: [Matric Number]  
**Institution**: [Institution Name]

## 📧 Contact

For questions or issues, please open an issue on GitHub or contact through the repository.

---

**Submission Date**: January 22, 2026  
**Course**: Machine Learning / Data Science Project