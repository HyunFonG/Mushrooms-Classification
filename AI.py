
# coding: utf-8

# In[31]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from itertools import product
from pandas.io.parsers import read_csv
from sklearn import preprocessing

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier

from sklearn.model_selection import cross_val_score


# In[32]:

# filename = input('Please enter your knowledge base file')
filename = 'mushrooms.csv'
data = read_csv(filename)


# In[33]:

for i in range(0, len(data.columns)):
    le = preprocessing.LabelEncoder()
    le.fit(data.ix[:, i])
    data.ix[:, i] = le.transform(data.ix[:, i])
    
data_target = data['class']
data_feature = data.drop('class', 1)


# In[34]:

cfl = DecisionTreeClassifier()
predict = cross_val_score(cfl, data_feature, data_target, scoring='f1', cv=5)
print(predict)


# In[35]:

# Training classifiers
clf1 = DecisionTreeClassifier()
clf2 = KNeighborsClassifier(n_neighbors=7)
clf3 = SVC(kernel='rbf', probability=True)
eclf = VotingClassifier(estimators=[('dt', clf1), ('knn', clf2),
                                    ('svc', clf3)],
                        voting='soft', weights=[2, 1, 2])


# In[36]:

clf1.fit(data_feature, data_target)
clf2.fit(data_feature, data_target)
clf3.fit(data_feature, data_target)
eclf.fit(data_feature, data_target)


# In[37]:

# Plotting decision regions
x_min, x_max = data_feature.ix[:, 0].min() - 1, data_feature.ix[:, 0].max() + 1
y_min, y_max = data_target.min() - 1, data_target.max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))


# In[39]:

f, axarr = plt.subplots(2, 2, sharex='col', sharey='row', figsize=(10, 8))

for idx, clf, tt in zip(product([0, 1], [0, 1]),
                        [clf1, clf2, clf3, eclf],
                        ['Decision Tree', 'KNN (k=7)',
                         'Kernel SVM', 'Soft Voting']):

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    axarr[idx[0], idx[1]].contourf(xx, yy, Z, alpha=0.4)
    axarr[idx[0], idx[1]].scatter(data_feature.ix[:, 0], data_feature.ix[:, 1], c=y, alpha=0.8)
    axarr[idx[0], idx[1]].set_title(tt)

plt.show()


# In[ ]:



