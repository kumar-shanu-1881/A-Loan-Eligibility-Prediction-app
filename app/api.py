import os
import sys
import joblib
import pandas as pd
from flask import Flask, request, jsonify


#adding the src to python's path that can we import it 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.feature_Engineering import featureEng

app = Flask(__name__)

# Load the master pipeline once when the server starts
model_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'loan_production_pipeline.pkl')
pipeline = joblib.load(model_path)

# health-check endpoint
@app.route('/health', methods=['GET'])
def health():
    # Return 200 OK immediately.
    return jsonify({"status": "alive"}), 200

@app.route('/')
def home():
    return "🏦 Loan Eligibility API is actively running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        #Receive the JSON data from Streamlit
        data = request.get_json()
        
        #Convert it into a Pandas DataFrame so the pipeline can read it
        input_df = pd.DataFrame([data])

        #pass df to feature eng
        input_df=featureEng(input_df)
        
        #Pass it through the Logistic Regression pipeline
        prediction = pipeline.predict(input_df)[0]
        probability = pipeline.predict_proba(input_df)[0][1]
        
        # Send the results back as JSON
        return jsonify({
            'prediction': int(prediction),
            'probability': float(probability)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # Run the Flask API on port 5000