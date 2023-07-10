#This script will focus on creating the model
#Will start with a keras convid2d model and attempt to make a model using pytorch later

#Imports here
import tensorflow as tf
import numpy as np

def main():
    #this is all just a test for now
    #Declare constants
    #Path to cleaned data
    DATA_PATH = "Data_Gathering\\Data\\De_Dup\\"

    #Load cleaned data
    print("Loading data...")
    X = np.load(f"{DATA_PATH}X\\X.npy")
    Y = np.load(f"{DATA_PATH}Y\\Y.npy")

    #basic split of 60/20/20
    temp = len(X)
    print(temp)
    print(f"{temp*0.6}: 60%")
    print(f"{temp*0.2}: 20%")
    print(f"{temp*0.8}: 80%")
    print(f"{(temp*0.6)+(temp*0.2)}: 60% + 20%")
    print()
    print(f"{temp//5}: 20%")
    print(f"{temp//5*3}: 60%")
    print(f"{temp//5*4}: 80%")
    print()
    #this one is the formula, get the 1% value, then multiply to the percentage you want
    print(f"{temp//100*80}: 80%")



#function to load data
def load_data(path):
    pass

#function to split data into (train/test/validation) sets
def data_split(x, y, percentages = (60,20,20)):
    #percentage is a tuple and should equal 100 in the end, create validator to make sure this is true
    #Check if percentage tuple adds up too 100
    if(sum(list(percentages)) != 100):
        #raise an error here
        print("ERROR")
    pass

if __name__ == "__main__":
    print("Code started")
    main()
    print("Code executed successfully")
    print("Big brain success!")