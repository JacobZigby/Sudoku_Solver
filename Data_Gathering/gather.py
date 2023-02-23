from Grid import Grid
import numpy as np

#the main function
def main():
    PATH = "Data"
    
    for i in range(100):
        save_batch(PATH, f"Batch_{i}")
        print(f"Batch_{i} completed")

# This gathering of data will be very plain and simple just to do some first level testing
# I will later return to optimize in a way to make sure the results are all unique
#I'll do this either by looking for a method to determin how a grid is unique or just pass the solver through it ten times and seeing if all ten results are identical
def save_batch(path, itter_name, batch_size = 1000, times_repeated = 10):
    #create a x and y list to be saved
    X = []
    Y = []

    #check to see that the batchsize is divisable by repetition
    if batch_size % times_repeated != 0:
        raise ValueError(f"batch_size ({batch_size}) is not divisable by times_repeated ({times_repeated})")

    #run loop batch_size times
    for _ in range(batch_size // times_repeated):
        grid = Grid()
        for _ in range(times_repeated):
            #append the new problem
            X.append(grid.random_removal())
        
        #Extend the list with the number of repetitions
        Y.extend([grid.get_grid()]*times_repeated)
        
    #save the batch here
    np.save(path+f"\\X\\{itter_name}", X)
    np.save(path+f"\\Y\\{itter_name}", Y)




#will keep this here for references
def reference():
    #create a grid to see if import worked successfully
    test1 = Grid()
    #testing grid object
    print(test1)
    
    test2 = Grid()
    print(test2)

    #path
    path = "Data\\test"

    test_list = [test1.random_removal(), test2.random_removal()]
    
    #test numpy savez
    np.save("Data\\test.npy",test_list)

    test_load = np.load("Data\\test.npy", mmap_mode="r")
    print(test_load[0])

if __name__ == "__main__":
    main()
    print("Code successfully executed")
