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
        #if this error is raised, I suggest reviewing the settings for the gather script and rerunning it
        raise ValueError(f"X ({len(X)}) and Y ({len(Y)}) are of unequal length")
    
    #in each tuple indexs; 0 = train, 1 = test, 2 = validation
    xs,ys= data_split(X,Y, shuffle=True)
    print(xs[1])


#function to split data into (train/test/validation) sets
def data_split(x, y, percentages = (80,10), shuffle = False):
    #Function will return a nested tuple where the first layer will be for x, y and the next for train,test,validate

    if len(percentages) not in [3,2]:
        #might be using the wrong exception type here
        raise IndexError(f"Expected 3 values from percentages arg, Received: {len(percentages)}")
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
    #get the 1% value, then multiply to the percentages demanded 
    q1 = data_size//100*percentages[0]
    q2 = (data_size//100*percentages[1]) +  q1

    #making each split here, and storing into tuples
    return (x[:q1],x[q1:q2],x[q2:]),(y[:q1],y[q1:q2],y[q2:])



if __name__ == "__main__":
    print("Code started")
    main()
    print("Code executed successfully")
    print("Big brain success!")