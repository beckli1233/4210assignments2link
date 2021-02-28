#-------------------------------------------------------------------------
# AUTHOR: Beize Li
# FILENAME: Decision_tree
# SPECIFICATION: trainning data and find the lowest accuracy.
# FOR: CS 4200- Assignment #2
# TIME SPENT: 4 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []
    acc = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =
    for i in dbTraining:
        s = []
        if i[0] == 'Young':
            s.append(1)
        elif i[0] == 'Prepresbyopic':
            s.append(2)
        elif i[0] == 'Presbyopic':
            s.append(3)
        if i[1] == 'Myope':
            s.append(1)
        elif i[1] == 'Hypermetrope':
            s.append(2)
        if i[2] == 'Yes':
            s.append(1)
        elif i[2] == 'No':
            s.append(2)
        if i[3] == 'Reduced':
            s.append(1)
        elif i[3] == 'Normal':
            s.append(2)
        X.append(s)
    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =
    for i in dbTraining:
        if i[4] == "Yes":
            Y.append(1)
        elif i[4] == 'No':
            Y.append(2)

    #loop your training and test tasks 10 times here
    for i in range (10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)
       #read the test data and add this data to dbTest
       #--> add your Python code here
       dbTest =[]
       with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                 if i > 0:  # skipping the header
                    dbTest.append(row)
       class_predicted = []
       confusion_matrix = [[0] * 2 for i in range(2)]
       for data in dbTest:
           #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
           #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here


           save =[]
           if data[0] == 'Young':
               save.append(1)
           elif data[0] == 'Prepresbyopic':
               save.append(2)
           elif data[0] == 'Presbyopic':
               save.append(3)
           if data[1] == 'Myope':
               save.append(1)
           elif data[1] == 'Hypermetrope':
               save.append(2)
           if data[2] == 'Yes':
               save.append(1)
           elif data[2] == 'No':
               save.append(2)
           if data[3] == 'Reduced':
               save.append(1)
           elif data[3] == 'Normal':
               save.append(2)
           predict_i = clf.predict([save])[0]
           save.clear()
           class_predicted.append(predict_i)

               # compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
               # --> add your Python code here
           truelabel_TP = []
           if data[4] == "Yes":
                truelabel_TP = 1
           elif data [4] == "No":
                truelabel_TP = 2
           confusion_matrix[truelabel_TP-1][predict_i-1] += 1

       accur = (confusion_matrix[0][0] + confusion_matrix[1][1]) / (
                confusion_matrix[0][0] + confusion_matrix[1][0] + confusion_matrix[0][1] + confusion_matrix[1][1])
       acc.append(accur)

        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here

       acc.sort()
    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that:

         #final accuracy when training on contact_lens_training_1.csv: 0.2
         #final accuracy when training on contact_lens_training_2.csv: 0.3
         #final accuracy when training on contact_lens_training_3.csv: 0.4
    #--> add your Python code here
    print("Final accuracy when training on",ds,acc[0])
    acc.clear()


