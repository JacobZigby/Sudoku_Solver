from Grid import Grid
import numpy as np

#the main function
#primary focus to collect and clean data
def main():
    PATH = "Data"
    ITTER_NAME = "Batch_"
    # for loop to save the batches
    # for i in range(100, 1000):
    #     save_batch(PATH, f"Batch_{i}")
    #     print(f"Batch_{i} completed")

    #call the combination method
    #combine_files(PATH, ITTER_NAME, 1000)
    # print(remove_dup([2,3,4,5,2,1,6,7,5],[1,2,3,4,5,6,7,8,9]))
    # temp1, temp2 = remove_dup([6,9,4,2,0,6,9,5,8,7,6,9,6,1,3,6,9,4,0],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])

    X_all = np.load(PATH+"\\X\\All_Data.npy")
    Y_all = np.load(PATH+"\\Y\\All_Data.npy")

    print(len(X_all))

    Cleaned_X_all, Cleaned_Y_all = remove_dup(X_all, Y_all)

    #to check if any changes happened
    print(f"Changes found: {len(X_all) == len(Cleaned_X_all)}")
    print(len(Cleaned_X_all))
    
    np.save(PATH+f"\\X\\New_All_Data", Cleaned_X_all)
    np.save(PATH+f"\\Y\\New_All_Data", Cleaned_Y_all)

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

# This method will combine all batches into one file
# I could program it using OS to just check for all the files and loop like that, but honestly I made it, and I know how many there are so let's not waste our time
def combine_files(path, itter_name, num_batches: int) -> None:
    #initalize the lists
    X = []
    Y = []
    #extraction loop
    for i in range(num_batches):
        X.extend(np.load(path+f"\\X\\{itter_name}{i}.npy"))
        Y.extend(np.load(path+f"\\Y\\{itter_name}{i}.npy"))
        print(f"{itter_name}{i} done loading!")

    #save a rough final file (will clean else where)
    np.save(path+f"\\X\\All_Data", X)
    np.save(path+f"\\Y\\All_Data", Y)
    print("Final save complete")

### DOESN'T WORK WITH NP ARRAYS, CONCLUSION CREATE A LIST OF ALL INDEXES THAT NEED TO BE REMOVED

#removes duplicates from list1 and removes the appropriate one from list2
#will only work for girds
def remove_dup(list1:np.ndarray, list2:np.ndarray):
    #make sure that both list are the same length
    if len(list1) != len(list2):
        raise ValueError(f"len of list1 ({len(list1)}) and list2 ({len(list2)}) are not equivalent")
    
    #create a list that will hold all the indexs to remove
    to_remove = []
    #create a masking layer
    mask = np.ones(len(list1),np.bool8)

    #original design was to remove as we go, so I started backwards to avoid shape issues, but now we remove at the end
    for iter1 in range(len(list1)-1, 0, -1):
        #only take the grids from the list as we only need it for comparions
        for iter2 in range(iter1-1,-1,-1):
            #check to make sure all values are true in the comparison (can also use np.array_equal(A,B))
            #also check to make sure that botho grid in the next list are also not the same
            if ((list1[iter2] == list1[iter1]).all() and (list2[iter2] == list2[iter1]).all()):
                print("activated")
                #add original index to the removal list
                to_remove.append(iter1)
                #break out as that's all we need for this iteration
                break
        #add a print statment to see progress
        print(f"iter: {iter1} completed!")
    
    #update mask layer with values to be removed
    mask[to_remove] = False
    #remove values here
    list1 = list1[mask]
    list2 = list2[mask]

    #return as a tuple that we'll seprate upon return outside
    return list1,list2


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
