from mesa import Model
from mesa.space import SingleGrid
from agents import SchellingAgent
from mesa.datacollection import DataCollector

class SchellingModel(Model):
    ## Define initiation, requiring all needed parameter inputs
    def __init__(self, width = 30, height = 30, density = 0.7, desired_share_alike = 0.5, group_one_share = 0.7, radius = 1, seed = None):
        ## Inherit seed trait from parent class and ensure seed is integer
        if seed is not None:
            seed = int(seed)
        super().__init__(rng=seed)
        ## Define parameter values for model instance
        self.width = width
        self.height = height
        self.density = density
        self.desired_share_alike = desired_share_alike
        self.group_one_share = group_one_share
        self.radius = radius
        ## Create grid
        self.grid = SingleGrid(width, height, torus = True)
        ## Instantiate global happiness tracker
        self.happy = 0
        ## Define data collector, to collect happy agents and share of agents currently happy
        self.datacollector = DataCollector(
            model_reporters = {
                "happy" : "happy",
                "share_happy" : lambda m : (m.happy / len(m.agents)) * 100
                if len(m.agents) > 0
                else 0
            }
        )
        ## Place agents randomly around the grid, randomly assigning them to agent types.
        for cont, pos in self.grid.coord_iter():
            if self.random.random() < self.density:
                if self.random.random() < self.group_one_share:
                    self.grid.place_agent(SchellingAgent(self, 1), pos)
                else:
                    self.grid.place_agent(SchellingAgent(self, 0), pos)
        ## Initialize datacollector
        self.datacollector.collect(self)

    ## Define a step: reset global happiness tracker, agents move in random order, collect data
    def step(self):
        self.happy = 0
        self.agents.shuffle_do("move")
        self.datacollector.collect(self)
        ## Run model until all agents are happy
        self.running = self.happy < len(self.agents)
