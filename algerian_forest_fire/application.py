from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

application = Flask(__name__)
app = application

## Import ridge regressor and standard scaler
ridge_model = pickle.load(open('models/Ridge.pkl', 'rb'))
scaler_model = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route("/")
def index():
    # Renders the initial form
    return render_template('home.html')

@app.route("/predictdata", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        try:
            # 1. Extract values from the HTML form using the 'name' attributes
            temperature = float(request.form.get('Temperature'))
            rh = float(request.form.get('RH'))
            ws = float(request.form.get('Ws'))
            rain = float(request.form.get('Rain'))
            ffmc = float(request.form.get('FFMC'))
            dmc = float(request.form.get('DMC'))
            isi = float(request.form.get('ISI'))
            region = float(request.form.get('Region'))
            
            # Convert categorical 'Classes' string ("fire"/"not_fire") to numeric encoding
            classes_str = request.form.get('Classes')
            classes = 1.0 if classes_str == 'fire' else 0.0

            # 2. Package inputs into an array in the exact order the scaler/model expects
            # Ensure this array sequence matches your training dataset columns perfectly
            features = [[temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]]

            # 3. Transform data and predict
            new_data_scaled = scaler_model.transform(features)
            result = ridge_model.predict(new_data_scaled)

            # 4. Return results back to the home template
            return render_template('home.html', results=round(result[0], 2))

        except Exception as e:
            return f"An error occurred: {str(e)}. Please check that all inputs match your model's expectations."
            
    else:
        # If method is GET, just display the empty form
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")