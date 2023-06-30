# Sudoku_Solver
A project whose aim is to determine the efficiency between a model that solves sudoku and a sudoku solver method. also aim to deploy so users can take pictures of real life problems and get an answer in response. maybe implement a hint system too
<br>
Read [HowToUse](HowToUse.md) if you wish to create your own model and dataset
<br>
Will release model once completed
### TO DO

Creating the fundementals
1. Create all five generator methods (On hold, but Done)
2. Create a validator (Done)
3. Create a solver (Done)
4. From the generator output succefully create a semi filled board (a method to remove values at random) (Done)
5. Test validator and solver on problems generated (Done)
6. Store mulitple problems (Done)
7. Prep data for a model (In-progress)
8. Create model
9. Test model vs solver on testing data
10. Check results
11. Create report with visuals

### Side projects

1. Create Gui for users to use models themselves (In-Progress Check Sudoku_Game repo)
2. Allow users to play any sudoku they find by taking a picture with their mobile device and having it transfered
3. Implement a hint method
4. Create a difficulty predictor

### NEWS

1. Update, finished collecting all the data (for now). Now I plan to focus on cleaning said data, by checking for duplicates and potentially seeing how many of the problems have more than one solution. (might also catagorize them in terms of how many values are missing)
2. Update, upon checking for duplicates I am happy to conclude none were found in my sample space, nervous about making the model but we are almost done!
