from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('Model_CP1.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    total_log_volume = float(request.form.get('total_log_volume'))
    max_volume       = float(request.form.get('max_volume'))
    num_log_features = float(request.form.get('num_log_features'))
    avg_volume       = float(request.form.get('avg_volume'))
    num_event_types  = float(request.form.get('num_event_types'))

    features = np.array([total_log_volume, max_volume,
                         num_log_features, avg_volume,
                         num_event_types]).reshape(1, 5)

    prediction = model.predict(features)[0]

    if prediction == 0:
        result = 'No Fault Detected'
        level  = 'safe'
    elif prediction == 1:
        result = 'Minor Fault Detected'
        level  = 'warning'
    else:
        result = 'Severe Fault Detected'
        level  = 'critical'

    return render_template('index.html', result=result, level=level)

import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
