## Use numpy to represent vectors as arrays
import numpy as np
## Using experimental continuous space implementation
from mesa.experimental.continuous_space import ContinuousSpaceAgent

class Boid(ContinuousSpaceAgent):
    ## Define initiation. Inherit space and model properties from parent class
    def __init__(
        self,
        model,
        space,
        position=(0, 0),
        speed=1,
        direction=(1, 1),
        vision=1,
        separation=1,
        cohere=0.03,
        separate=0.015,
        match=0.05,
    ):
        ## Initialize parameters: position, speed, direction, vision radius, minimum separation, factors for coherence, separation, and matching, and list of nearby agents
        super().__init__(space, model)
        self.position = position
        self.speed = speed
        self.direction = direction
        self.vision = vision
        self.separation = separation
        self.cohere_factor = cohere
        self.separate_factor = separate
        self.match_factor = match
        self.neighbors = []

    def flock(self):
        ## Get list of other agents within vision radius
        neighbors, distances = self.get_neighbors_in_radius(radius=self.vision)
        self.neighbors = [n for n in neighbors if n is not self]

        # If no neighbors, maintain current direction
        if not neighbors:
            self.position += self.direction * self.speed
            return
        ## Get difference vector viz. all neighbors
        delta = self.space.calculate_difference_vector(self.position, agents=neighbors)
        ## Get vector for maximizing coherence (e.g. moving toward neighbors), weighted by coherence factor
        cohere_vector = delta.sum(axis=0) * self.cohere_factor
        ## Get separation vector (i.e. vector moving away from agents within minimum separation range), weighted by separation factor
        separation_vector = (
            -1 * delta[distances > self.separation].sum(axis=0) * self.separate_factor
        )
        ## Get matching vector (i.e. vector for moving parallel to neighbors), weighted by matching factor
        match_vector = (
            np.asarray([n.direction for n in neighbors]).sum(axis=0) * self.match_factor
        )
        # Update direction based on the three behaviors, weighted by number of neighbors
        self.direction -= (cohere_vector + separation_vector + match_vector) / len(
            neighbors
        )
        # Normalize direction vector
        self.direction /= np.linalg.norm(self.direction)
        # Move boid
        self.position += self.direction * self.speed
