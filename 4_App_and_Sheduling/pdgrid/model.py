import mesa
from agents import PDAgent
from mesa.discrete_space import OrthogonalMooreGrid

class PDModel(mesa.Model):
    ## Define possible activation regimes
    activation_regimes = ["Sequential", "Random", "Simultaneous"]
    ## Define payoffs. Note that model results are sensitive to these! Making DD too high or lowering CD can make systems devolve into defection
    payoff = {("C", "C"): 1, ("C", "D"): 0, ("D", "C"): 1.6, ("D", "D"): 0}
    ## Initialize model, inheriting seed property from parent class
    def __init__(self, width=40, height=40, order="Simultaneous", payoffs=None, seed=None):
        super().__init__(rng=seed)
        ## Define Acivation order
        self.order = order
        ## Initialize grid
        self.grid = OrthogonalMooreGrid((width, height), torus=True, random=self.random)
        ## If alternative payoff structure is entered on model startup, overwrite above structure
        if payoffs is not None:
            self.payoff = payoffs
        ## Create one agent for every cell in model
        PDAgent.create_agents(
            self, len(self.grid.all_cells.cells), cell=self.grid.all_cells.cells
        )
        ## Set up datacollector, collects count of cooperating agents
        self.datacollector = mesa.DataCollector(
            {"Cooperators": lambda m: len(
                    [a for a in m.agents if a.move == "C"])}
        )
        ## Set model to running
        self.running = True
        ## Initialize datacollector
        self.datacollector.collect(self)
    ## Define step as function of activation regime
    def step(self):
        if self.order == "Sequential":
            self.agents.do("pick_move")
        elif self.order == "Random":
            self.agents.shuffle_do("pick_move")
        elif self.order == "Simultaneous":
            self.agents.do("pick_move")
            self.agents.do("update")
        else:
            raise ValueError(f"Unknown activation order: {self.order}")
        ## Collect data
        self.datacollector.collect(self)
