# HOW TO USE
Note: you will need to have some version of python installed to run this
1. Fork and Clone repo where ever you desire
### Setting up enviroment
1. <i><b>(This step is not necessary but suggested)</b></i> open command prompt and navigate your way to where the repo was cloned and run this snippet: 
~~~
python -m venv sudoku_env
~~~
Note: you can navigate your way through directories using the cd command [Examples](https://www.lifewire.com/change-directories-in-command-prompt-5185508#:~:text=In%20the%20command%20prompt%20window%2C%20type%20cd%20followed%20by%20the,the%20one%20you're%20in.&text=If%20you%20want%20to%20go,back%20to%20the%20original%20option.) <br>

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
* batch_size: (LINE: 17) total size of a single batch
* times_repeated: (LINE: 17) Number of times a problem is created per individual solution; if used batch_size must be divisible by times_repeated

* PERSONAL STATES USED (NUM_BATCHES: 1000, batch_size: 1000, times_repeated: 10)
<br>

1. Activate the env (if created and not already activated)

2. Make your way to the working directory: Sudoku_Solver

3. Run Script using this snippet:
~~~
python Data_Gathering\gather.py
~~~

4. let the code do it's magic (may take some time, but progression will show on the command line if running)

Once everything is completed if you wish to delete all the data, just empty the data folders

### Setting up model
TO BE ADDED

