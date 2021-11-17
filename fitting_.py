import numpy as np
import pandas as pd
# from statsmodels.api import OLS
from sklearn.linear_model import LinearRegression, LogisticRegression,LogisticRegressionCV,Perceptron
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.naive_bayes import MultinomialNB,GaussianNB
from sklearn.neural_network import MLPClassifier



"""
Here is the file that you can use to load the data in as the targets and data.
You can choose what classifiers you want to run it on and save the data to a <classifier>.txt

"""

def load_():
    df = pd.read_csv("chess_games.csv")
    targets = df.Name
    data = df.drop(columns=['Name', 'Color', 'Variant', 'Moves'])
    return data, targets

if __name__ == '__main__':
    data, targets = load_()
    data = pd.get_dummies(data,columns=data.columns)
    xtrain,xtest,ytrain,ytest = train_test_split(data,targets)
    params = {'n_neighbors': [2,3,4],
            'weights' :['uniform','distance'],
            'leaf_size' : [30,40,50,60],

    }

    # knnGSCV = GridSearchCV(KNeighborsClassifier(),params,n_jobs=-1,scoring='f1')
    #
    # print(knnGSCV.fit(xtrain,ytrain))
    # print(KNeighborsClassifier(n_neighbors=4,weights='distance',algorithm='brute').fit(xtrain,ytrain).score(xtest,ytest)) # this is the best


    # print(LinearRegression().fit(xtrain,ytrain).score(xtest,ytest))

    # print(LogisticRegression(multi_class="multinomial").fit(xtrain,ytrain).score(xtest,ytest)) # this is good
    # print(MultinomialNB().fit(xtrain,ytrain).score(xtest,ytest)) #this is oay
   # print(GaussianNB().fit(xtrain,ytrain).score(xtest,ytest)) Not this

    # print(Perceptron().fit(xtrain,ytrain).score(xtest,ytest))

    # print(MLPClassifier().fit(xtrain,ytrain).score(xtest,ytest))