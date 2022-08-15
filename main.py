#summary:
#create a suduko generator
#conditions all rows, cols, and squares need to equal 45 

# Imports here
import numpy as np
import random
# using this for multidimensinal arrays and calculations

def main():
    print("main code started")
    
    #option 1: fill up a grid trying to only look at the possibilites and when failed try again from scratch
    #option 2: fill up grid but with the ability to backtrack
    #option 3: fill in the diagonal squares first and fill in the rest after
    #option 4: fill in all rows and then shuffle to a solution
    #option 5: do one number type at a time

    #create a set that contains all possible values in a row, col or 3X3 space
    values = {1,2,3,4,5,6,7,8,9}

    #create the grid
    grid = np.zeros((9,9), dtype = np.int8)

    #create offsets for viewing space of 3X3
    row_offset = 0
    col_offset = 0

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
            print(f"row offset: {row_offset}")

        for col in range(len(grid[row])):

            #update col offset when needed
            if not(col % 3):
                #when col is divisable by 3, update col multiplier by one
                col_offset += 1
                print(f"col offset: {col_offset}")

                #take the current quadrent we are filling up    
                current_square = grid[(row_offset-1)*3:row_offset*3, (col_offset-1)*3:col_offset*3]
                #turn into 1d and into a set
                current_square =  set(current_square.flatten())
                print("current square",current_square)

            #doesn't work, there would need to be another coditon on choosing which values to select
            #suggestion, maybe look at the last boxs on the east side and remove the values the last box
            #can choose from, or make sure that the selected value leaves a possibility for the last box at all times
            available_values = values - (set(grid[row]) | set(grid[:,col]) | current_square)
            print("available values",available_values)
            
            #if row is not divisable by three and the current quadrent
            # is in the middle quadrents then check last box to help in the selction
            #also add condition to not include last sqaure 
            # if (row % 3) and col <= 5 and col >= 3:
            #     print("condition met")
            #     #remake this section to work with quad 1 and 2 but not three, use the rows differences perhaps
            #     #available_values = available_values & set(grid[(row_offset-1)*3:row_offset*3, col_offset*3:(col_offset + 1)*3].flatten())
            #     union =  set(grid[(row_offset-1)*3:row_offset*3, col_offset*3:(col_offset + 1)*3].flatten()) | set(grid[(row_offset-1)*3:row_offset*3, (col_offset-2)*3:(col_offset - 1)*3].flatten())
            #     available_values = available_values & union

            #test to see if all of last quad is in current row (can keep zero as it's guarenteed to be in the last three)
            #redo first if statment, but make it applicable for the first quad
            #and add a counter so that the length works only when neccesary
            if (row % 3) and col <= 5 and col >=3 and set(grid[(row_offset-1)*3:row_offset*3, col_offset*3:].flatten()) - set(grid[row]):
                print("condition met")
                union =  set(grid[(row_offset-1)*3:row_offset*3, col_offset*3:(col_offset + 1)*3].flatten())
                available_values = available_values & union


            #this is for the divisible rows and not the first row
            #not working properly, seems that avaliable values is bugging up, I need to add the condition for the first grid as well
            elif not(row % 3) and (row > 0) and col < 6:
                print("condition 2 met")
                #first test will be on the first two rows of the square above
                #hard code for testing purposes
                #I'll come back to this
                print("last two columns/rows", set(grid[0:2,-3:].flatten()))
                available_values = available_values & set(grid[0:2,-3:].flatten())
            #what I could also do is, if you take the last two rows after the first one is initalized

            # use this if completion is impossible and you wish to see the errors
            # if len(available_values) == 0:
            #     grid[row][col] = -1
            # else:
            print(grid)
            grid[row][col] = list(available_values).pop(np.random.randint(len(available_values)))



    print(grid)
    #option 5 use matrixs

    #option 6 the shuffler

#Test to see what __name__ is
print(__name__)

if __name__ == "__main__":
    main()
    print("Code succesfully exucuted")
