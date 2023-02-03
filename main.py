#summary:
#create a suduko generator
#conditions all rows, cols, and squares need to equal 45 

# Imports here
from ast import While
from os import dup
from re import template
import numpy as np
import random

# using this for multidimensinal arrays and calculations

def main():
    print("main code started")
        
    #option 1: fill up a grid trying to only look at the possibilites and when failed try again from scratch (done)
    #option 2: fill up grid but with the ability to backtrack
    #option 3: fill in the diagonal squares first and fill in the rest after
    #option 4: fill in all rows and then shuffle to a solution
    #option 5: do one number type at a time
    grid = generator()
    print(random_removal(grid))
    print(grid)

def generator():
    #main suduko generator method, this one should be my most optimized version
    #will start off by solveing the diagonals first and then generating solutions with backtracking
    
    #initalize grid
    grid = np.zeros((9,9), dtype = np.int8)

    #create the values that can be chosen from
    values = {1,2,3,4,5,6,7,8,9}

    #A temporary placeholder for diagonal quads
    temp_quad = list(values)

    #create a for loop to populate the diagonals
    for i in range(3):
        #the offset to where the quadrants begin
        offset = i * 3

        #shuffle the last version of temp quad before placing it in the grid
        np.random.shuffle(temp_quad)
        grid[offset : 3 + offset, offset : 3 + offset] = np.reshape(temp_quad, (3,3))

    #call the filler function
    fill_grid(grid,0,3)
    
    return grid

#Create a recursive backtracking method to fill in the grid
def fill_grid(grid, row, col):
    #base case/ending scenario
    if col == 9:
        #end of column has been reached, readjusting values
        col = 0
        row += 1
        if row == 9:
            #all squares have been filled, thus end the cycle
            return True

    #skip already filled in squares
    if grid[row, col] != 0:
        return fill_grid(grid, row, col + 1)

    #put all available values into a list to chose for
    bag_of_values = avaliable_values(grid, row, col)
    np.random.shuffle(bag_of_values)
    #fill in missing value using only valid values
    for value in bag_of_values:
        grid[row,col] = value
        if fill_grid(grid, row, col+1):
            return True
        #if current iterations did not work, reset value
        grid[row, col] = 0
    #return false as no value was found
    return False


#check for all avaliable values for a location
def avaliable_values(grid, row, col):
    #Default values
    values = {1,2,3,4,5,6,7,8,9}
    #remove values found on the selected row
    values = values - set(grid[row])
    #remove values found on selected column
    values = values - set(grid[:,col])

    #identify the quad
    col_quad = col // 3
    row_quad = row // 3
    
    #create a set to easily remo
    quad_set = set(grid[row_quad*3:(row_quad+1)*3, col_quad*3:(col_quad+1)*3].flatten())
    values = values - quad_set

    return list(values)

#Check to see if a hypothetical value can fit into the grid at selected location
def is_valid(grid:np.ndarray, row, col, value):
    #check to see if new value already exists in row
    if value in grid[row]:
        #if value exists return false
        print(f"Value {value} exists on row: {row}")
        return False
    
    #check to see if new value already exists in col
    if value in grid[:,col]:
        #if value exists return false
        print(f"Value {value} exists on col: {col}")
        return False

    #identify current quad by getting the floor division of current coordinates
    col_quad = col // 3
    row_quad = row // 3
    
    #create a list to easily check if value exists inside
    quad_list = grid[row_quad*3:(row_quad+1)*3, col_quad*3:(col_quad+1)*3].flatten()

    #check if the value exists inside the quad
    if value in quad_list:
        print(f"Value {value} exists in quad {(col_quad,row_quad)}")
        return False
    
    #if none of the conditions passed, return true as value does not exist yet
    return True

#method to remove values from valid sudoku grids, returns a new grid
def random_removal(grid, remove_num = 0):
    #create a copy of the grid as to not overwrite the original
    new_grid = grid.copy()
    
    #total number of squares in a grid
    TOTAL_SQUARES = 9 * 9

    #Check to see if remove_num contains a valid number, if not randomly assign one
    if(not remove_num or remove_num > TOTAL_SQUARES-17):
        #through a quick search we see that the minumue number of given squares that are needed to solve a sudoku is 17
        remove_num = np.random.randint(20,TOTAL_SQUARES-16)

    print(remove_num)

    return new_grid

#create a method that solves the sudoku the same way a player does and gives a grading scheme to it

#for the methods these are temporary names, will also come back to see if I can better optomize some of these
def gen1():
    #create a set that contains all possible values in a row, col or 3X3 space
    values = {1,2,3,4,5,6,7,8,9}

    #initalize a grid
    grid = None

    #initalize and set to true
    is_scrape = True

    while is_scrape:

        #create the grid
        grid = np.zeros((9,9), dtype = np.int8)

        #create offsets for viewing space of 3X3
        row_offset = 0
        col_offset = 0

        #create status checkers
        is_scrape = False #checks to see if the grid is scrapped on this attempt

        #itterate through each row and column to input a value
        for row in range(len(grid)):
            #reset offset for 3X3 viewing spaces
            col_offset = 0

            #intalize current sqaure to change in for loops
            current_square = None

            #update row offset when needed
            if not(row % 3):
                #when row is divisable by 3, update the row multiplier by one
                row_offset += 1
                #print(f"row offset: {row_offset}")

            for col in range(len(grid[row])):

                #update col offset when needed
                if not(col % 3):
                    #when col is divisable by 3, update col multiplier by one
                    col_offset += 1
                    #print(f"col offset: {col_offset}")

                    #take the current quadrent we are filling up    
                    current_square = grid[(row_offset-1)*3:row_offset*3, (col_offset-1)*3:col_offset*3]
                    #turn into 1d and into a set
                    current_square =  set(current_square.flatten())
                    #print("current square",current_square)

                #doesn't work, there would need to be another coditon on choosing which values to select
                #suggestion, maybe look at the last boxs on the east side and remove the values the last box
                #can choose from, or make sure that the selected value leaves a possibility for the last box at all times
                available_values = values - (set(grid[row]) | set(grid[:,col]) | current_square)
                #print("available values",available_values)
                
                #if row is not divisable by three and the current quadrent
                # is in the middle quadrents then check last box to help in the selction
                #test to see if all of last quad is in current row (can keep zero as it's guarenteed to be in the last three)
                #redo first if statment, but make it applicable for the first quad
                #and add a counter so that the length works only when neccesary
                if (row % 3) and col <= 5 and col >=3 and set(grid[(row_offset-1)*3:row_offset*3, col_offset*3:].flatten()) - set(grid[row]):
                    #print("condition met")
                    union =  set(grid[(row_offset-1)*3:row_offset*3, col_offset*3:(col_offset + 1)*3].flatten())
                    available_values = available_values & union


                #this is for the divisible rows and not the first row
                #not working properly, seems that avaliable values is bugging up, I need to add the condition for the first grid as well
                elif not(row % 3) and (row > 0) and col < 6:
                    #print("condition 2 met")
                    #first test will be on the first two rows of the square above
                    #hard code for testing purposes
                    #I'll come back to this
                    #print("last two columns/rows", set(grid[0:2,-3:].flatten()))
                    available_values = available_values & set(grid[0:2,-3:].flatten())
                #what I could also do is, if you take the last two rows after the first one is initalized

                # use this if completion is impossible and you wish to see the errors
                # if len(available_values) == 0:
                #     grid[row][col] = -1
                # else:
                #print(grid)
                if not available_values:
                    #print("list empty")
                    is_scrape = True
                    break

                grid[row][col] = list(available_values).pop(np.random.randint(len(available_values)))

            #if the grid is scraped just start over
            if is_scrape:
                break

        #put back one tap to just see the final result
        #print(grid)

    return grid

#come back to this:
def gen4():
    #generate 9 X 9 gride with rows to shuffle
    #cool tool, but not neccesary for what I have in mind
    #grid = np.tile([1,2,3,4,5,6,7,8,9], (9,1))

    VALUES = (1,2,3,4,5,6,7,8,9)

    #generate a base board and shuffle all rows at least once
    grid = np.array([random.sample(VALUES, 9) for i in range(len(VALUES))])

    #a column value that will act as a check to start a recursive function
    col_dup = -1

    #step one check if the first column is equal to 45
    #step two check for duplicate values and missing values
    #step three replace a duplicate for a missing (on the same row)
    #repeat until all columns are searched through 

    for col in range(len(grid)): 
        #create an array to hold the count of all numbers
        n_count = np.bincount(grid[:,col], minlength=10)
        #to keep in mind about n_count: 1) index zero counts for all instances of the number zero
        #example, when index is equal to 1, whatever the output is, that's how many 1's exist in that column
        available_values = [x for x in range(1,10) if n_count[x] == 0]
        #create a shuffler for the availale_values that checks if there exists a value, if no values then skip this itteration
        if(len(available_values)>0):
            random.shuffle(available_values)
        else:
            print("This itteration has been skipped: Due to no missing value in column")
            continue

        for row in range(len(grid)):
            #check for when the value shows up more than once
            if(n_count[grid[row,col]] > 1):
                #search for the replacment value
                #could do this in one line, but it would look messy
                bool_con = [value in grid[row,col:] for value in available_values]
                #if a value exists in the row, search for it's location and do the swap
                if True in bool_con:
                    #traverse the row starting from the current column
                    for s_col in range(col, len(grid)):
                        if grid[row, s_col] in available_values:
                            #remove the value from available_values
                            available_values.remove(grid[row, s_col])

                            #do the value's reassignments to other neccesary variables
                            #here we remove one as the current column is lossing this value
                            n_count[grid[row,col]] -= 1
                            #here we add one as the current column is gaining this value
                            n_count[grid[row,s_col]] += 1

                            #replacement down here
                            tmp = grid[row,col]
                            grid[row,col] = grid[row, s_col]
                            grid[row, s_col] = tmp

                            #leave the for loop as replacment has been completed
                            break
        
        print(n_count)

        #Activate the condition value and set the column that needs 
        if(set(n_count[1:]) != {1} and col_dup == -1):
            col_dup = col
    

    #call recursive backtracking function here to solve the last duplication values

    return grid

#recursive column dup solver
def col_dup_solver(grid, col = 0, last_row = None):
    #check grid to see if it matches the shape requierments (to add when possible)

    #a while loop to traverse the columns of the grid (this while loop disolves the need for recursion)
    #change the while loop for the is conditon just below with an else that calls this function but with plus one to col
    #and if the col value is greater than the grid len then just return the grid

    #if the col has stepped out of bounds return the final grid result
    if(col == len(grid)):
        return grid

    #check for exsistence of duplicates
    n_count = np.bincount(grid[:,col], minlength=10)[1:]
    
    #if no duplicates exist check next column
    if(set(n_count) == {1}):
        return col_dup_solver(grid, col + 1)
        
    #create a dup_num var and assign a temp variable
    dup_num = 0

    #create an missing var and assign a temp variable
    missing_num = 0

    #check all number counts in the column
    for i in range(len(n_count)):
        if(n_count[i]>1 and dup_num == 0):
            #assign proper dup number
            dup_num = i + 1 

        #check if value is a missing value from column
        if(n_count[i] == 0 and missing_num == 0):
            #assign missing value to var
            missing_num = i + 1
            #can potentially change this to a list to add randomness to the generations later if I have time
        
        #who knows, trying to save some time
        if(dup_num != 0 and missing_num != 0):
            break

    print(f"D: {dup_num}    M: {missing_num}")
    #find the location of the first dup num and the first missing num
    # going to use numpy.where too get coordinates

    #get the y(row) coordinates for the duplicates and missing value using the current column
    dup_cord = np.where(grid[:,col] == dup_num)
    #check to see this value matches with the last value, if so, use next value

    #get the x(col) coordinates for the missing value using the row of first found duplicate
    missing_cord = np.where(grid[dup_cord[0][0]] == missing_num)

    print(grid[dup_cord[0][0],missing_cord[0][0]])
    print(grid[dup_cord[0][0],col])
    #do the value transferes here
    print(f"col: {col}, row: {missing_cord[0][0]}")
    
    #change dup for missing
    grid[dup_cord[0][0],col]= missing_num

    #change missing for dup
    grid[dup_cord[0][0], missing_cord[0][0]] = dup_num


    print(grid)
    #after the transfere check the column to see if any duplicates exist if they do, call the function from that column
    #if none found call the funciton on the same col
    #check if new column has any duplicates

    if(missing_cord[0][0]< col and set(np.bincount(grid[:,missing_cord[0][0]], minlength=10)[1:]) != {1}):
        return col_dup_solver(grid,missing_cord[0][0],dup_cord[0][0])

    return col_dup_solver(grid, col)


def authenticator(grid):
    #the grid should be a 2d array with the shape of 9 by 9
    #potential update (make it so sudukos with missing values in boxes can still be accepted)

    #step 1 check what type of object grid is and turn into numpy array if need be
    #step 2 check each column and row and make sure all values are unique from 1-9
    #step 3 check each quad and make sure each value are unique from 1-9

    #offsets to be used to determin which quad to check at the specified time
    quad_col_offset = 0
    quad_row_offset = 0
    #we're currently just wanting to solve something right now so here's the quick and dirty verion
    for i in range(len(grid)):
        row = np.bincount(grid[i], minlength=10)
        col = np.bincount(grid[:,i],minlength=10)


        #checks to see that only one of each possibility exists at a time
        if(set(row[1:]) != {1} or set(col[1:]) != {1} ):
            #print a statement to help locate error locations
            print(f"Invalid value found in row or column: {i}")
            #returns a false testing is the test passes
            return False

        #checking quads
        if(i != 0 and i % 3 == 0):
            quad_col_offset = 0
            quad_row_offset += 1

        #The logical checking of the quad
        quad_set = set(
            #turning it into an array of unique values
            np.bincount(
                grid[
                    quad_row_offset * 3 : (quad_row_offset + 1) * 3,
                    quad_col_offset * 3 : (quad_col_offset + 1) * 3
                ].flatten(),
                minlength=10
            )
        )

        if(quad_set != {1}):
            #print a statment to help locate which quadrant has an error
            print(f"Invalid value found in quad: {i+1}") #plus one for quad identity
            #return a false for when a duplicate is found in a quadrant
            return False
        #quad section here
        #add the extra value for the next itteration
        quad_col_offset += 1

    return True
#Test to see what __name__ is
print(__name__)

if __name__ == "__main__":
    # #original
    # # tmp_grid = np.array(
    # #     [[3, 2, 7, 6, 5, 8, 1, 4, 9],
    # #     [9, 1, 3, 4, 6, 7, 8, 2, 5],
    # #     [5, 8, 6, 3, 7, 1, 2, 9, 4],
    # #     [8, 6, 5, 2, 1, 4, 9, 7, 3],
    # #     [7, 4, 9, 5, 8, 2, 3, 1, 6],
    # #     [4, 5, 2, 9, 3, 6, 7, 8, 1],
    # #     [1, 9, 8, 7, 4, 3, 6, 5, 2],
    # #     [2, 3, 1, 8, 9, 5, 4, 6, 7],
    # #     [6, 7, 4, 1, 2, 9, 5, 3, 8]]
    # # )
    # tmp_grid = np.array(
    #     [[3, 2, 7, 6, 5, 8, 1, 4, 9],
    #     [9, 1, 3, 4, 6, 7, 8, 2, 5],
    #     [5, 8, 6, 3, 7, 1, 2, 9, 4],
    #     [8, 6, 5, 2, 1, 4, 9, 7, 3],
    #     [7, 4, 9, 5, 8, 2, 3, 1, 6],
    #     [4, 5, 2, 9, 3, 6, 7, 8, 1],
    #     [1, 9, 8, 7, 4, 3, 6, 5, 2],
    #     [2, 3, 1, 8, 9, 5, 4, 6, 7],
    #     [6, 7, 4, 1, 2, 9, 5, 3, 8]]
    # )
    # print(authenticator(tmp_grid))
    # tmp_grid = np.array(
    #     [[3, 2, 7, 6, 5, 8, 1, 4, 9],
    #     [9, 1, 3, 4, 6, 7, 8, 2, 5],
    #     [5, 8, 6, 9, 7, 1, 2, 3, 4],
    #     [8, 6, 5, 2, 1, 4, 9, 7, 3],
    #     [7, 4, 9, 5, 8, 2, 3, 1, 6],
    #     [4, 5, 2, 3, 9, 6, 7, 8, 1],
    #     [1, 9, 8, 7, 4, 3, 6, 5, 2],
    #     [2, 3, 1, 8, 9, 5, 4, 6, 7],
    #     [6, 7, 4, 1, 2, 9, 5, 8, 3]]
    # )
    # col_dup_solver(tmp_grid, 4)
    main()
    print("Code succesfully exucuted")