from pandas.io.parsers import read_csv
import pandas as pd

import numpy as np

from sklearn import tree
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score

# filename = input('Please enter your knowledge base file')
filename = 'mushrooms.csv'
data = read_csv(filename)

for i in range(0, len(data.columns)):
    le = preprocessing.LabelEncoder()
    le.fit(data.ix[:, i])
    data.ix[:, i] = le.transform(data.ix[:, i])

data_target = data['class']
data_feature = data.drop('class', 1)

cfl = tree.DecisionTreeClassifier()

predict = cross_val_score(cfl, data_feature, data_target, scoring='f1', cv=5)
print(predict)
# cfl.fit(data_feature, data_target)
#
# true_positive = 0
# true_negative = 0
# false_positive = 0
# false_negative = 0
#
# data_predict = cfl.predict(data_feature)
# # print(data_target[0])
# for i in range(0, len(data_target)):
#     if data_predict[i] == data_target[i]:
#         if data_target[i] == 'p':
#             true_positive += 1
#         else:
#             true_negative += 1
#     else:
#         if data_target[i] == 'p':
#             false_positive += 1
#         else:
#             false_negative += 1
#
# print((true_positive+true_negative)/(true_positive+true_negative+false_positive+false_negative))