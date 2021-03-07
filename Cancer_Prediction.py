#%%
#import libraries and load the data set
import sklearn
from sklearn.datasets import load_breast_cancer

#loading the data set
data=load_breast_cancer()
#%%
#Organizing the dataset
label_names=data['target_names']
labels=data['target']
feature_names=['feature_names']
features=data['data']
#%%
print(label_names)
print(labels)
print(feature_names)
print(features)
#%%
#Organising the data into sets
from sklearn.model_selection import train_test_split

#Splitting the data
train,test,train_labels,test_labels = train_test_split(features,labels,test_size = 0.33,random_state = 42)
#%%
#Building the model
#import the model
from sklearn.naive_bayes import GaussianNB

#initializing the classifier
gnb = GaussianNB()

#training the classifier

#making the predictions
predictions = gnb.predict

#print the prediction
#%%
#Evaluting the trained model's accuruacy

#importing the accuracy measuring function
from sklearn.metrics import accuracy_score
#evaluting the accuracy
print(accuracy_score,(test_labels,predictions))