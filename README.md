# P7-Openclassrooms-API
This repository has been created in the context of the 7th project of my Data Scientist training with Openclassrooms. 
The goal of this project is to use datas from a former Kaggle competition (https://www.kaggle.com/c/home-credit-default-risk/data) to build a classification model. 
The model is a binary classification with a positive class corresponding to a customer with loan repayment difficulties. 
The model must take into consideration a business optimization considering false negatives have a bigger impact than a false positive on bank revenues. 
Then the model is deployed throught an API to make predictions and a dashboard to display results visually.

This repository concerns the API which has been built with Flask library. This API gives predictions in 2 situations:
- Prediction for a customer in the training set, the API needs a GET HTTP request with the customer id as an argument : https://p7-openclassrooms-api.herokuapp.com/api/predict-existing/
- Prediction for a new customer, the API needs a POST HTTP request with customer's datas (with same preprocessing than training set) : https://p7-openclassrooms-api.herokuapp.com/api/predict-new/

The other repositories about this project can be found on the following links :
- Modeling : https://github.com/RobinPbt/P7-Openclassrooms
- Dashboard : https://github.com/RobinPbt/P7-Openclassrooms-Dashboard

The dashboard application can be found on the following link : https://p7-openclassrooms-dash.herokuapp.com/

# Run locally

If you want to run locally the API, you can directly download the files and launch your console with the command "python app.py", the URLS would be (replace XXXX by the corresponding port) :
- http://127.0.0.1:XXXX/api/predict-existing/ --> in order to get a result you must specify parameter id_customer in your GET request (ex: http://127.0.0.1:XXXX/api/predict-existing/?id_customer=110503)
- http://127.0.0.1:XXXX/api/predict-new/ --> this would only work with a POST HTTP request containing the file of the new customer in the preprocessed format
