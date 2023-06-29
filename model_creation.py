#This script will focus on creating the model
#Will start with a keras convid2d model and attempt to make a model using pytorch later

#Imports here
import tensorflow as tf
import numpy as np

def main():
    #Declare constants
    DATA_PATH = "Data_Gathering\\Data\\De_Dup\\"

    #Load cleaned data
    print("Loading data...")
    X = np.load(f"{DATA_PATH}X\\X.npy")
    Y = np.load(f"{DATA_PATH}Y\\Y.npy")


#function to load data
def load_data(path):
    pass

if __name__ == "__main__":
    print("Code started")
    main()
    print("Code executed successfully")
    print("Big brain success!")