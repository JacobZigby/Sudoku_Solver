# HOW TO USE
Note: you will need to have some version of python installed to run this
1. Fork and Clone repo where ever you desire
### Setting up enviroment
1. <i><b>(This step is not necessary but suggested)</b></i> open command prompt and navigate your way to where the repo was cloned and run this snippet: 
~~~
python -m venv sudoku_env
~~~
2. <i><b>(This step is not necessary but suggested)</b></i> Activate the environment by running this snippet in the console:
~~~
sudoku_env\Scripts\activate
~~~
3. pip install all requirements (necessary libraries found in the requirements.txt)
~~~
#Run this snippet if you're currently in the working directory
pip install -r requirements.txt
~~~
4. NOTE: once environment is set up, you will only need to do step too to use it again if you ever wish to restart

### Gathering Data
Feel free to modify formula, found in the gather.py script, as needed. Will provide short explanation and line reference
FORMULA: Total_entries = <i>NUM_BATCHES</i> * <i>batch_size</i> <br>
* Total_entries: Total numper of individual entries that will be created
* NUM_BATCHES: (LINE: 12) Number of times a batch will be saved
* batch_size: (LINE: 17)

Once everything is completed if you wish to delete all the data, just empty the data folders

### Setting up model
TO BE ADDED

