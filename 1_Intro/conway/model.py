from mesa import Model
from agents import ConwayAgent
from mesa.space import SingleGrid

class ConwayModel(Model):
    #Define required inputs for model (size of space, share of agents beginning alive, random seed)
    def __init__(self, width = 20, height = 20, start_alive = 0.3, seed = None):
        #Ensure seed is integer and set it.
        if seed is not None:
            seed = int(seed)
        super().__init__(rng = seed)
        #Initialize grid
        self.grid = SingleGrid(width, height, torus = True)
        #Iterate through grid creating agents and randomly setting them to living/dead states
        for cont, (x, y) in self.grid.coord_iter():
            conway = ConwayAgent(self, (x, y))
            if self.random.random() < start_alive:
                conway.state = 1
            else:
                conway.state = 0
            self.grid.place_agent(conway, (x, y))
        self.running = True

    #Model step: first all agents decide whether they will live or die, then all implement change
    def step(self):
        self.agents.do("determine_next_state")
        self.agents.do("live_or_die")      
