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

    #check to see that both files are of the same size
    if len(X) != len(Y):
        raise ValueError(f"X ({len(X)}) and Y ({len(Y)}) are of unequal length")
    
    #basic split of 80/10/10
    temp = len(X)
    #this one is the formula, get the 1% value, then multiply to the percentage you want
    print(f"{temp//100*80}: 80%")

    print("Testing X and Y values:")
    print(X[0])
    print(Y[0])

    print("Test of data_split method")
    xs,ys= data_split(X,Y, shuffle=True)
    print(xs[0][0])
    print(ys[0][0])

#come back to fix percentages later
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
        #unzip and reassigning back to x and y
        x,y = zip(*temp)

    #get index location for each split
    data_size = len(x)
    q1 = data_size//100*percentages[0]
    q2 = (data_size//100*percentages[1]) +  q1

    #making each split here, and storing into tuples
    return (x[:q1],x[q1:q2],x[q2:]),(y[:q1],y[q1:q2],y[q2:])



if __name__ == "__main__":
    print("Code started")
    main()
    print("Code executed successfully")
    print("Big brain success!")