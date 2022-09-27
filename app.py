from flask import Flask, request, jsonify
from utils import *

import pandas as pd
import numpy as np
import seaborn as sns
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

app.config.from_object('config')

@app.route('/api/predict-existing/', methods=['GET'])
def predict_existing():
    
    if 'id_customer' in request.args:
        
        customer = request.args['id_customer']
        
        # Load saved classification model
        load_clf = pickle.load(open('./Models/final_model.pkl', 'rb'))
        
        # Load datas of customer
        customer_features = find_customer_features(customer)
        
        # Make predictions
        probas = load_clf.predict_proba(customer_features.values.reshape(1, -1))[:,1]
        predictions = (probas >= PREDICT_THRESHOLD).astype(int)
        
        probas = float(probas[0])
        predictions = int(predictions[0])
        
        return jsonify({
            'status' : 'ok',
            'datas': {
                'prediction' : predictions,
                'proba' : probas
            }
        })
         
    else:
        return jsonify({
            'status': 'error',
            'message': 'You must specify parameter id_customer'
        }), 500

    
@app.route('/api/predict-new/', methods = ['POST'])
def predict_new():
    
    # Load model, imputer and preprocessor
    imputer = pickle.load(open('./Models/imputer.pkl', 'rb'))
    preprocessor = pickle.load(open('./Models/preprocessor.pkl', 'rb'))
    load_clf = pickle.load(open('./Models/final_model.pkl', 'rb'))
    
    # Load file
    file_1 = request.files['data']
    x = pd.read_csv(file_1)
    x.index = x['SK_ID_CURR']
    x.drop('SK_ID_CURR', axis=1, inplace=True)  

    # Make predictions
    probas = load_clf.predict_proba(x)[:,1]
    predictions = (probas >= PREDICT_THRESHOLD).astype(int)

    probas = float(probas[0])
    predictions = int(predictions[0])
    
    return jsonify({
    'status' : 'ok',
    'datas': {
        'prediction' : predictions,
        'proba' : probas
    }
})
    
if __name__ == "__main__":
    app.run(debug=True)


