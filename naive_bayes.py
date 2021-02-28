#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
dbtraining =[]
target = {
    'Sunny':1,
    'Overcast':2,
    'Rain':3,
    'Hot':1,
    'Mild':2,
    'Cool':3,
    'High':1,
    'Normal':2,
    'Strong':1,
    'Weak':2
}
PT = {
    'Yes':1,
    'No':2
}
TP ={
    1:'Yes',
    2:'No'
}
#reading the training data
#--> add your Python code here
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         dbtraining.append (row)
#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =

X=[]
for item in dbtraining:
    temp=[]
    temp.append(target[item[1]])
    temp.append(target[item[2]])
    temp.append(target[item[3]])
    temp.append(target[item[4]])
    X.append(temp)
#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
Y=[]
for i in dbtraining:

    Y.append(PT[i[5]])
#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
dbTest=[]
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         dbTest.append (row)
#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
Z = []
for i in dbTest:
    temp = []
    temp.append(target[i[1]])
    temp.append(target[i[2]])
    temp.append(target[i[3]])
    temp.append(target[i[4]])
    Z.append(temp)
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
    predicted_proba =clf.predict_proba([temp])[0]
    predicted = clf.predict([temp])[0]
    if predicted_proba[predicted-1] >=0.75:
     print(i[0].ljust(15) + i[1].ljust(15) + i[2].ljust(15) + i[3].ljust(15) + i[4].ljust(15) + TP[predicted].ljust(15) + str(predicted_proba[predicted-1]).ljust(15))
