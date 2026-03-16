from mesa.discrete_space import CellAgent

class PDAgent(CellAgent):
    ## Initialize agent, inherit model property from parent class
    def __init__(self, model, cell=None):
        super().__init__(model)
        ## Initialize score at 0, store location in grid, randomly determine opening move, initialize next move
        self.score = 0
        self.cell = cell
        self.move = self.random.choice(["C", "D"])
        self.next_move = None
    def pick_move(self):
        ## Get list of neighbors, plus self (if an agent does better than all neighbors, it does not change strategies)
        neighbors_plus_me = [*list(self.cell.neighborhood.agents), self]
        ## Get the most successful neighbor
        best_neighbor = max(neighbors_plus_me, key=lambda a: a.score)
        ## Set move for next round as most successful neighbor's current move
        self.next_move = best_neighbor.move
        ## If agents are not all activated at once, they calculate payoffs and update move now
        if self.model.order != "Simultaneous":
            self.update()
    def update(self):
        ## Set move to planned next move
        self.move = self.next_move
        ## Add payoffs from games in this round
        self.score += self.add_to_score()
    def add_to_score(self):
        ## Get neighbors, now not including self
        neighbors = self.cell.neighborhood.agents
        ## If activating simultaneously, look at neighbors' planned next moves to determine payoffs
        if self.model.order == "Simultaneous":
            moves = [neighbor.next_move for neighbor in neighbors]
        ## If activating sequentially or randomly, look at neighbors' actual moves for payoffs
        else:
            moves = [neighbor.move for neighbor in neighbors]
        ## Calculate payoffs for each neighbor based on payoff matrix defined in model, sum them
        return sum(self.model.payoff[(self.move, move)] for move in moves)
