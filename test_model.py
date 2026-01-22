"""
Test script to verify model loading and prediction functionality
"""
import joblib
import numpy as np

def test_model():
    """Test the saved model"""
    print("=" * 60)
    print("BREAST CANCER MODEL TEST")
    print("=" * 60)
    
    # Load the model
    print("\n1. Loading model...")
    try:
        model_data = joblib.load('model/breast_cancer_model.pkl')
        model = model_data['model']
        scaler = model_data['scaler']
        features = model_data['features']
        print("✓ Model loaded successfully")
        print(f"✓ Features: {features}")
    except Exception as e:
        print(f"✗ Error loading model: {e}")
        return
    
    # Test with sample data
    print("\n2. Testing with sample data...")
    
    # Sample 1: Typical benign tumor values
    sample1 = {
        'mean radius': 12.5,
        'mean texture': 18.0,
        'mean perimeter': 81.0,
        'mean area': 476.0,
        'mean smoothness': 0.088
    }
    
    # Sample 2: Typical malignant tumor values
    sample2 = {
        'mean radius': 20.0,
        'mean texture': 25.0,
        'mean perimeter': 130.0,
        'mean area': 1200.0,
        'mean smoothness': 0.12
    }
    
    samples = [
        ("Benign-like sample", sample1),
        ("Malignant-like sample", sample2)
    ]
    
    for name, sample in samples:
        print(f"\n{name}:")
        print(f"  Input: {sample}")
        
        # Prepare input
        input_array = np.array([sample[f] for f in features]).reshape(1, -1)
        input_scaled = scaler.transform(input_array)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        prediction_proba = model.predict_proba(input_scaled)[0]
        
        result = "Benign" if prediction == 1 else "Malignant"
        confidence = prediction_proba[prediction] * 100
        
        print(f"  Prediction: {result}")
        print(f"  Confidence: {confidence:.2f}%")
    
    print("\n" + "=" * 60)
    print("TEST COMPLETED SUCCESSFULLY")
    print("=" * 60)

if __name__ == "__main__":
    test_model()
