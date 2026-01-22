# Quick Start Guide

This guide will help you get the Breast Cancer Prediction System up and running in minutes.

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning)

## Installation (5 minutes)

### Step 1: Clone the Repository
```bash
git clone https://github.com/moladeji2302025-ctrl/Breast-Cancer-Prediction-System.git
cd Breast-Cancer-Prediction-System
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Verify Model File
```bash
# Check that the model file exists
ls model/breast_cancer_model.pkl
```

## Running the Application

### Option 1: Web Application (Recommended)

Start the Flask server:
```bash
python app.py
```

Then open your web browser and navigate to:
```
http://localhost:5000
```

### Option 2: Jupyter Notebook

Launch Jupyter:
```bash
jupyter notebook
```

Then open: `model/model_building.ipynb`

### Option 3: Test Script

Run the test script:
```bash
python test_model.py
```

## Using the Web Interface

1. **Enter Tumor Features**: Fill in the 5 feature values in the form
   - Mean Radius (typical: 6-28)
   - Mean Texture (typical: 9-40)
   - Mean Perimeter (typical: 43-188)
   - Mean Area (typical: 143-2500)
   - Mean Smoothness (typical: 0.05-0.16)

2. **Get Prediction**: Click "Predict Tumor Type"

3. **View Results**: 
   - Prediction: Benign or Malignant
   - Confidence: Percentage confidence
   - Input Summary: Your entered values

## Sample Values for Testing

### Benign Tumor Example
- Mean Radius: 12.5
- Mean Texture: 18.0
- Mean Perimeter: 81.0
- Mean Area: 476.0
- Mean Smoothness: 0.088

**Expected**: Benign with high confidence

### Malignant Tumor Example
- Mean Radius: 20.0
- Mean Texture: 25.0
- Mean Perimeter: 130.0
- Mean Area: 1200.0
- Mean Smoothness: 0.12

**Expected**: Malignant with high confidence

## Troubleshooting

### Issue: Module not found
**Solution**: Install requirements
```bash
pip install -r requirements.txt
```

### Issue: Model file not found
**Solution**: Ensure you're in the correct directory and the model file exists
```bash
cd /path/to/Breast-Cancer-Prediction-System
ls model/breast_cancer_model.pkl
```

### Issue: Port 5000 already in use
**Solution**: Use a different port
```python
# Edit app.py, change the last line to:
app.run(debug=debug_mode, host='0.0.0.0', port=8080)
```

## Development Mode

To run in development mode with debug enabled:
```bash
export FLASK_DEBUG=true  # Linux/Mac
# OR
set FLASK_DEBUG=true     # Windows

python app.py
```

## Production Deployment

For production, use a WSGI server:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Next Steps

- Deploy to Vercel, Heroku, or another platform
- Update `BreastCancer_hosted_webGUI_link.txt` with deployment details
- Explore the Jupyter notebook for detailed model analysis

## Support

For issues or questions:
- Check the README.md for detailed documentation
- Review the SUMMARY.md for project overview
- Check the code comments in source files

---

**Happy Predicting! 🩺**
