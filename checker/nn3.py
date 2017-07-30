import numpy as np
import pandas as pd

def sigmoid(z):
    return 1/(1+np.exp(-z))

def forward(X,W1, W2):
    Xt = np.vstack((1,np.transpose(X)))
    z2 = np.matmul(W1, Xt)
    a2 = sigmoid(z2)
    a2b = np.vstack((1,a2))
    z3 = np.matmul(W2,a2b)
    yHat = sigmoid(z3)
    return(yHat)


def compute(ip):
    databaseDisease = pd.read_csv('C:\MinorProject\minor\checker\dem.csv')
    databaseSymptom = pd.read_csv('C:\MinorProject\minor\checker\symptomLabel.csv')

    a = np.array(databaseDisease)
    b = np.array(databaseSymptom)

    diseaseLabel = a.T[0:1]
    symptomLabel = np.delete(b[0:1], 0, axis=1)


    w1 = np.loadtxt('C:\MinorProject\minor\checker\weights_W1')
    w2 = np.loadtxt('C:\MinorProject\minor\checker\weights_W2')
    W1 = np.matrix(w1)
    W2 = np.matrix(w2)

    symptomInput = []
    inputNet = []
    symptomInput = ip.split('+')



    for item in symptomLabel[0]:
        if item in symptomInput:
            inputNet.append(1)
        else:
            inputNet.append(0)
    print(inputNet)

    X = np.matrix(inputNet)
    outputNet = forward(X,W1,W2).T
    outputNet = np.round(outputNet)

    s=[]

    s = np.squeeze(np.asarray(outputNet))

    possibleDiseases = []
    counter = 0
    for j in s:
        if j == 1:
            possibleDiseases.append(diseaseLabel[0][counter])
        counter = counter + 1
    return (possibleDiseases)
    


    
