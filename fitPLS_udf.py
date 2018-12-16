# -*- coding: utf-8 -*-
"""
Function to fit PLS model.
Usage: fitPLS(input)
"""
import numpy as np
import pandas as pd
import json

from sklearn.cross_decomposition import PLSRegression 

 
def fitPLS(input_data):
    ### Step 1 - unpack input JSON to normal data array
    input_df = pd.DataFrame(input_data)
    
    colnames = list(input_df.columns.values)  
    colnames[len(colnames) - 1] = 'Intercept'
    
    train_arr = np.zeros(shape = input_df.shape)

    for i in range(train_arr.shape[0]):
        for j in range(train_arr.shape[1]):
            train_arr[i,j] = float(input_df.values[i,j]['value'])
            

    ### Step 2 - fit the model. X - independent variables; Y - output variable
    X, Y = train_arr[:, : - 1], train_arr[:, -1] 
    
    n_best = 2
    
    best_fit = PLSRegression(n_components = n_best, scale = False)
    best_fit.fit(X, Y)
    
    ### Step 3 - retrieve regression coefficients and pack them to JSON
    model_coef = best_fit.coef_
    y_intercept = best_fit.y_mean_ - np.dot(best_fit.x_mean_ , best_fit.coef_)
    
    model_vector = np.append(model_coef, y_intercept)
        
    model_list = model_vector.tolist()
    
    model_dict = dict(zip(colnames, model_list))
    model_js = json.dumps(model_dict)
        
    
    return model_js; 