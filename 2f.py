import numpy as np 
from sklearn import tree
import graphviz
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
import pydot

def encode(dataset):
	dataset['Age']=dataset['Age'].map({'< 21':0 , '21-35':1 ,'> 35':2})
	dataset['Income'] = dataset['Income'].map({'Low':0, 'Medium':1, 'High':2})
	dataset['Gender'] = dataset['Gender'].map({'Female':0, 'Male':1})

 
	dataset['Martial Status'] = dataset['Martial Status'].map({'Single':0, 'Married':1})


	if 'Buys' in dataset.columns: # Target column may or may not be part of dataframe
		dataset['Buys'] = dataset['Buys'].map({'No':0, 'Yes':1})

data=pd.read_csv('dataset.csv')
print(data)
encode(data)

Y=data["Buys"]

data=data.drop(labels=["Buys"] , axis=1)
data=data.drop(labels=["ID"] , axis=1)
print(data)

clf=DecisionTreeClassifier()


clf=clf.fit(data,Y)

print(clf.tree_.node_count)

row=[['< 21', 'Low','Female','Married']]
df_p=pd.DataFrame(row,columns=['Age','Income','Gender','Martial Status'])
encode(df_p)



print(clf.predict(df_p))
if clf.predict(df_p):
	print("buys")
else:
	print("dosent buy")
dot_data = tree.export_graphviz(clf, out_file ="tree.dot")
graph = graphviz.Source(dot_data)
graph
'''dot tree.dot -Tpng -o image.png'''
