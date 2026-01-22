from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join('model', 'breast_cancer_model.pkl')
try:
    model_data = joblib.load(model_path)
    model = model_data['model']
    scaler = model_data['scaler']
    features = model_data['features']
    print("Model loaded successfully")
    print(f"Features: {features}")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    scaler = None
    features = None

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html', features=features)

@app.route('/predict', methods=['POST'])
def predict():
    """Make prediction based on input features"""
    try:
        if model is None:
            return jsonify({
                'error': 'Model not loaded. Please ensure breast_cancer_model.pkl exists in the model directory.'
            }), 500
        
        # Get input data from form
        input_data = []
        for feature in features:
            value = float(request.form.get(feature, 0))
            input_data.append(value)
        
        # Convert to numpy array and reshape
        input_array = np.array(input_data).reshape(1, -1)
        
        # Scale the input data
        input_scaled = scaler.transform(input_array)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        prediction_proba = model.predict_proba(input_scaled)[0]
        
        # Get confidence
        confidence = prediction_proba[prediction] * 100
        
        # Determine result
        result = "Benign" if prediction == 1 else "Malignant"
        
        return jsonify({
            'prediction': result,
            'confidence': f"{confidence:.2f}",
            'input_features': dict(zip(features, input_data))
        })
        
    except Exception as e:
        return jsonify({
            'error': f'Error making prediction: {str(e)}'
        }), 400

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

if __name__ == '__main__':
    # For production, set debug=False and use a proper WSGI server
    # For development, you can set debug=True
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
