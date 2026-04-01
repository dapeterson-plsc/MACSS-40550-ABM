from mesa import Agent

class ConwayAgent(Agent):
    #Initialize agent, setting position, and state
    def __init__(self, model, pos, state = 0):
        super().__init__(model)
        self.x, self.y = pos
        self.state = None
        self.new_state = None
    def determine_next_state(self):
        # Count number of living neighbors
        live_neighbors = sum(neighbor.state for neighbor in self.model.grid.iter_neighbors((self.x, self.y), True))
        #Living agents decide whether they will stay alive or die next round
        if self.state == 1:
            if live_neighbors < 2 or live_neighbors > 3:
                self.new_state = 0
            else: self.new_state = 1
        #Dead agents decide whether to come back to life or not
        else:
            if live_neighbors == 3:
                self.new_state = 1
            else:
                self.new_state = 0
    #After making determination, implement it (used to simulate simultaneous action)
    def live_or_die(self):
        self.state = self.new_state
        
