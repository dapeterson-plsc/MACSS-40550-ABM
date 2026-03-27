*Code adapted from Mesa Examples project*

# Conway's game of life

## Summary
This model follows a simple series of rules and demonstrates how, using a few simple rules, cells can live or die. This particular version of the model starts with agents on the upper left of the grid and then allows the 'Rules of Life' (below) to play out. 

### Rules
**For a space that is populated:**
1) Each cell with one or no neighbors dies, as if by solitude.

2) Each cell with four or more neighbors dies, as if by overpopulation.

3) Each cell with two or three neighbors survives.

**For a space that is empty or unpopulated:**
1) Each cell with three neighbors becomes populated.

## How to run
1) To install dependencies, use pip and the requirements.txt file in this directory 
 
```
     pip install -r requirements.txt
```
2) To run the model interactively, run the following code in this directory:

```
     solara run app.py
```

Then open your browser to [http://127.0.0.1:8513/](http://127.0.0.1:8513/) and press Reset, then Start. (if you would like, you can change the number of agents, just click 'reset' after you change the number to set up the model.)

## Files
**agents.py** sets up agents (cellular automata) for the game, including the rules of living / dying

**model.py** sets up the model itself and calls on agents in each time step

**app.py** sets up visualization of agents

## Your Tasks

**1) Comment the code**
In each of the files presented here, add comments to explain the function of each line of code.

**2) Make some modifications**
Once you have commented the code, do the following:
 1. In the app.py file, change the color scheme of the model's visualization to something of your choice.
 2. In the agents.py file, change the cells' decision rule such that they survive if 1-2 neighbors are alive and become repopulated with exactly 2 live neighbors, and change the grid from a Moore to a von Neumann neighborhood.
 3. In the model.py file, modify the grid so that the edges of the space do not wrap around.

## Other resources
* https://playgameoflife.com/info 
* https://ccl.northwestern.edu/netlogo/models/Life
