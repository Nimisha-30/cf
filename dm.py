# -*- coding: utf-8 -*-
"""DM_CA2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yjURQSrK32wVxnemhSkKGYlNXicg1Duu

# K Means Clustering
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('/content/Iris.csv', index_col='Id')
data.head()

x = data.iloc[:, [ 0, 1, 2, 3]].values
x[:2]

data.info()

iris_crosstab = pd.crosstab(index = data['Species'], columns='count')
iris_crosstab

iris_setosa=data.loc[data["Species"]=="Iris-setosa"]
iris_virginica=data.loc[data["Species"]=="Iris-virginica"]
iris_versicolor=data.loc[data["Species"]=="Iris-versicolor"]

sns.FacetGrid(data, hue='Species').map(sns.distplot, 'SepalLengthCm').add_legend()
sns.FacetGrid(data, hue='Species').map(sns.distplot, 'SepalWidthCm').add_legend()
sns.FacetGrid(data, hue='Species').map(sns.distplot, 'PetalLengthCm').add_legend()
sns.FacetGrid(data, hue='Species').map(sns.distplot, 'PetalWidthCm').add_legend()

sns.set_style("whitegrid")
sns.pairplot(data,hue="Species");
plt.show()

wcss=[]
for i in range(1,11):
  km = KMeans(n_clusters=i, init='k-means++',max_iter=300, n_init=10, random_state=0)
  km.fit(x)
  wcss.append(km.inertia_)

plt.plot(range(1,11), wcss)

kmeans = KMeans(n_clusters=3,init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(x)

y_kmeans

#Visualising the clusters
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'purple', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'orange', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Iris-virginica')

#Plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'red', label = 'Centroids')

plt.legend()

kmeans.inertia_

kmeans.cluster_centers_

#Visualising the clusters
plt.scatter(x[y_kmeans == 0, 2], x[y_kmeans == 0, 3], s = 100, c = 'purple', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 2], x[y_kmeans == 1, 3], s = 100, c = 'orange', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 2], x[y_kmeans == 2, 3], s = 100, c = 'green', label = 'Iris-virginica')

#Plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 2], kmeans.cluster_centers_[:,3], s = 100, c = 'red', label = 'Centroids')

plt.legend()

fig = plt.figure(figsize = (10,10))
ax = fig.add_subplot(111, projection='3d')
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'purple', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'orange', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Iris-virginica')

#Plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'red', label = 'Centroids')
plt.show()

#Visualising the clusters
fig = plt.figure(figsize = (10,10))
ax = fig.add_subplot(111, projection='3d')
plt.scatter(x[y_kmeans == 0, 2], x[y_kmeans == 0, 3], s = 100, c = 'purple', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 2], x[y_kmeans == 1, 3], s = 100, c = 'orange', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 2], x[y_kmeans == 2, 3], s = 100, c = 'green', label = 'Iris-virginica')

#Plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 2], kmeans.cluster_centers_[:,3], s = 100, c = 'red', label = 'Centroids')

plt.legend()

"""# Naive Bayes"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

data.head()

X = data[['SepalLengthCm',	'SepalWidthCm',	'PetalLengthCm',	'PetalWidthCm']]
y = data[['Species']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier_nb = GaussianNB()
classifier_nb.fit(X_train, y_train)

y_pred = classifier_nb.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)

cm

acc

df = pd.DataFrame()
df['Real Values'] = y_test
df['Pred Values'] = y_pred
df.head()

"""# CART"""

from sklearn import tree

classifier_id3 = tree.DecisionTreeClassifier(criterion="entropy")

classifier_id3.fit(X_train, y_train)

plt.figure(figsize=(20, 10))
tree.plot_tree(classifier_id3, filled=True, max_depth=6)
plt.show()

y_pred = classifier_id3.predict(X_test)

print(accuracy_score(y_test, y_pred))

"""# Random Forest"""

from sklearn.ensemble import RandomForestClassifier

classifier_rdm = RandomForestClassifier()

classifier_rdm.fit(X_train, y_train)

y_pred = classifier_rdm.predict(X_test)
print(accuracy_score(y_test, y_pred))

for i in range(3):
  plt.figure()
  t = classifier_rdm.estimators_[i]
  tree.plot_tree(t, filled=True)
  plt.show()

"""# Bagging"""

from sklearn.ensemble import BaggingClassifier
clf = BaggingClassifier(n_estimators=10, random_state=22)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

acc = accuracy_score(y_test, y_pred)
acc

clf.estimators_

for i in range(2):
  t = clf.estimators_[i]
  tree.plot_tree(t, filled=True)
  plt.figure()

"""# Gradient Boosting"""

from sklearn.ensemble import GradientBoostingClassifier

clf = GradientBoostingClassifier(n_estimators=10, learning_rate=0.01, max_depth=5, random_state=42)

clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
acc

"""# AdaBoost"""

from sklearn.ensemble import AdaBoostClassifier

base_learner = tree.DecisionTreeClassifier(max_depth=1)
clf = AdaBoostClassifier(base_estimator= base_learner, n_estimators=10, learning_rate=0.01, random_state=42)

clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
acc

"""# Logistic Regression"""

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression(random_state = 0)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
acc = accuracy_score(y_test, y_pred)
acc

!pip install c45-decision-tree

from C45 import C45Classifier

clf = C45Classifier()
clf.fit(X_train, y_train)
s = cross_val_score(clf, X_train, y_train)
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
acc

"""# Ensemble"""

from sklearn.ensemble import VotingClassifier

estimators = [('logreg', logreg), ('naiveBayes', classifier_nb), ('decisionTree', classifier_id3), ('c45', clf)]

ensembleModel = VotingClassifier(estimators = estimators, voting='hard')

ensembleModel.fit(X_train, y_train)
y_pred = ensembleModel.predict(X_test)
acc = accuracy_score(y_test, y_pred)
acc

ensembleModel.score(X_test, y_test)

from sklearn.model_selection import cross_val_score

score = cross_val_score(ensembleModel, X_train, y_train, cv=10)

score

