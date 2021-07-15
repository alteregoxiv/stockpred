from flask import(
    render_template,
    request,
    redirect,
    url_for,
    jsonify
)

import numpy as np
import tensorflow
from tensorflow import keras
from keras.models import load_model
from datetime import date
import pickle
from sklearn.preprocessing import MinMaxScaler

def index():
    return render_template('index.html')

def todate():
    d = request.args['q'].split('-')
    #print("we have : " , d)

    sc = MinMaxScaler(feature_range = (0 , 1))

    model = load_model("./src/stock.h5")
    
    with open('./src/amzclose.pkl' , 'rb') as fi:
        ac = pickle.load(fi)

    ac = sc.fit_transform(ac)
    ac = ac.flatten()

    date1 = date(2019 , 1 , 31)
    date2 = date(int(d[0]) , int(d[1]) , int(d[2]))
    datediff = (date2 - date1).days
    #print("YOHOOOOO : " , datediff)
    
    for i in range(datediff):
        a = []
        l = len(ac)
        for j in range(l-100 , l):
            a.append(ac[j])

        anew = np.reshape(a , (1 , 100 , 1))
        ap = model.predict(anew)
        print(ap , i)
        ac = np.append(ac , ap[0][0])
    
    ac = np.reshape(ac , (-1 , 1))
    acn = sc.inverse_transform(ac)
    print(acn[len(acn)-1])

    return jsonify({"dc" : acn[len(acn)-1][0] , "da" : d})
