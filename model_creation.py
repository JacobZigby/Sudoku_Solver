#This script will focus on creating the model
#Will start with a keras convid2d model and attempt to make a model using pytorch later

#Imports here
import random
import tensorflow as tf
import numpy as np

def main():
    #Declare constants
    #Path to cleaned data
    DATA_PATH = "Data_Gathering\\Data\\De_Dup\\"

    #Load cleaned data
    print("Loading data...")
    X = np.load(f"{DATA_PATH}X\\X.npy")
    Y = np.load(f"{DATA_PATH}Y\\Y.npy")

    #basic split of 80/10/10
    temp = len(X)
    #this one is the formula, get the 1% value, then multiply to the percentage you want
    print(f"{temp//100*80}: 80%")

    print("Testing X and Y value type:")
    print(type(X[0]))
    print(Y[0])

    print("Test of data_split method")
    data_split(X,Y, shuffle=True)

#function to split data into (train/test/validation) sets
def data_split(x, y, percentages = (80,10,10), shuffle = False):
    #Function will return a nested tuple where the first layer will be for x, y and the next for train,test,validate
    #Check if percentage tuple adds up too 100
    if(sum(list(percentages)) != 100):
        raise ValueError(f"Percentage tuple {percentages} does not add up too 100")
    
    #shuffle here if true
    if shuffle:
        #zip x and y values and do a basic
        temp = list(zip(x,y))
        random.shuffle(temp)
        #unzip and reassing back to x and y
        x,y = zip(*temp)

        print("Test to see how the shuffle effects the values")
        print(type(x[0]))
        print(y[0])




if __name__ == "__main__":
    print("Code started")
    main()
    print("Code executed successfully")
    print("Big brain success!")