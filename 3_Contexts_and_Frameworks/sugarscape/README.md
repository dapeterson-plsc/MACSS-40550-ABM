*Code adapted from Mesa Examples project*

# SugarScape with Gini Index Tracker

This directory contains an implementation of Epstein and Axtell's (1996) model SucarScape from the book *Growing Artifical Societies*, in which agents attempt to survive in an environment defined by the distribution of sugar, a resource they need to survive. Agents vary in how far they can see on the map and how much sugar they require to stay alive. The model is a canonical attempt to to grow a society from the ground up in a specific spatial context, with emergent outcomes like inequality (tracked here as the Gini index over agents' sugar endowments) and carrying capacity.

In this version of the model, consumed sugar grows back at a rate of one unit per time step from an initial defined spatial distribution, instantiated in the text file in this directory. Agents move to the closest available spot within their vision that maximizes their potential to consume sugar, and die if they ever have zero or negative sugar.

## Your Task

Your task is to think of a non-trivial theoretical modification to the spatial map context in the model and implement it. This could mean changing the initial distribution of sugar, changing the growback rule, changing the borders of the map, or anything else. Basically, do not touch the agents.py file, but change anything you want to in model.py (or in the text file containing the sugar distribution). Come up with something interesting, and use the app to see if your assumptions are right!

## How to Run

To run the model interactively once you have a complete agents file, run the following code in this directory:

```
    $ solara run app.py
```

## Files

* ``agents.py``: Contains the agent class
* ``model.py``: Contains the model class
* ``app.py``: Defines classes for visualizing the model in the browser via Solara, and instantiates a visualization server.
* ``sugar-map.txt``: Raster file with the default sugar distibution for the model
