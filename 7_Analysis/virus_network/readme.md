*Code adapted from Mesa Examples project*

# Virus on a Network

An implementation of a classic model of a virus spreading through a social network. In the model, agents cycle through stages of infection\: susceptible to the virus, immune to it, and infected.

## Your Task

Currently, the model only places agents in one kind of network\: an Erdos-Renyi random network. Your job is to modify the code in the model to accommodate at least one other network structure. Add code to the model file allowing a user to select between different network types, and add functionality to the GUI to allow users to select between the options you define.

Then, if you have time, run a short batch run of the model varying network type and produce a wuick descriptive statistic or visualization about the difference in a variable of your choice across network shapes.

## How to Run

BE SURE TO INSTALL REQUIREMENTS FIRST! If you don't see the visualization, check that you have the requirements installed in your virtual environment!
```
    pip install -r requirements.txt
```

Launch the model (note that this will produce an error, as described above):
```
    solara run app.py
```

## Files

* ``agents.py``: Contains the agent class
* ``model.py``: Contains the model class
* ``app.py``: Defines classes for visualizing the model in the browser via Solara, and instantiates a visualization server.
