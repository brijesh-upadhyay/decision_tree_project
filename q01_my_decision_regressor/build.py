# %load q01_my_decision_regressor/build.py
# default imports
from sklearn.model_selection import GridSearchCV,cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

data = pd.read_csv("./data/house_pricing.csv")
np.random.seed(9)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=9)

param_grid = {"max_depth": [2, 3, 5, 6, 8, 10, 15, 20, 30, 50],
              "max_leaf_nodes": [2, 3, 4, 5, 10, 15, 20],
              "max_features": [4, 8, 20, 25]}

def my_decision_regressor(X_train, X_test, y_train, y_test,param_grid):
    classifier = DecisionTreeRegressor(random_state=9)

    grid_search = GridSearchCV(estimator=classifier, param_grid=param_grid,cv=5)
    grid_search.fit(X_train,y_train)
    y_prediction = grid_search.predict(X_test)
    return float(r2_score(y_test,y_prediction)),grid_search.best_params_

#my_decision_regressor(X_train, X_test, y_train, y_test,param_grid)
