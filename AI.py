from pandas.io.parsers import read_csv
import pandas as pd
import pydotplus

import numpy as np

from sklearn import tree
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score

# filename = input('Please enter your knowledge base file')
filename = 'mushrooms.csv'
data = read_csv(filename)
new_data = data.copy()

for i in range(0, len(data.columns)):
    le = preprocessing.LabelEncoder()
    le.fit(data.ix[:, i])
    new_data.ix[:, i] = le.transform(data.ix[:, i])


# print (data.drop('class', 1))

data_target = new_data['class']
data_feature = new_data.drop('class', 1)

cfl = tree.DecisionTreeClassifier()

predict = cross_val_score(cfl, data_feature, data_target, scoring='f1', cv=5)
# print(predict)

cfl = cfl.fit(data_feature, data_target)

print (list(np.unique(new_data['class'])))
# dot_data = tree.export_graphviz(cfl, out_file=None) 
dot_data = tree.export_graphviz(cfl, out_file=None, 
                         feature_names=list(data_feature.columns),  
                         class_names=list(np.unique(data['class'])),
                         filled=True, rounded=True,  
                         special_characters=True
                          )
graph = pydotplus.graph_from_dot_data(dot_data)  

graph.write_pdf("decision_tree.pdf")
