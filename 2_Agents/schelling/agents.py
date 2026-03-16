from mesa import Agent

class SchellingAgent(Agent):
    ## Initiate agent instance, inherit model trait from parent class
    def __init__(self, model, agent_type):
        super().__init__(model)
        ## Set agent type
        self.type = ________
    ## Define basic decision rule
    def move(self):
        ## Get list of neighbors within range of sight
        neighbors = self.model.grid.get_neighbors(
            _______________________________)
        ## Count neighbors of same type as self
        similar_neighbors = _________________________
        ## If an agent has any neighbors (to avoid division by zero), calculate share of neighbors of same type
        if ____________________
            share_alike = ______________________
        else:
            _________________
        ## If unhappy with neighbors, move to random empty slot. Otherwise add one to model count of happy agents.
        if share_alike < __________________:
            self.model.grid.move_to_empty(_____)
        else: 
            _______________  
