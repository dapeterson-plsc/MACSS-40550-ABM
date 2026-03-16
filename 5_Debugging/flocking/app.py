from model import BoidFlockers
from mesa.visualization import Slider, SolaraViz, make_space_component
from mesa.visualization.components import AgentPortrayalStyle

def agent_portrayal(agent):
    neighbors = len(agent.neighbors)
    return AgentPortrayalStyle(
        color = "blue" if neighbors <= 1 else "yellow",
        marker= "o",
        size= 20,
    )
    
model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "population_size": Slider(
        label="Number of boids",
        value=100,
        min=10,
        max=200,
        step=10,
    ),
    "width": 100,
    "height": 100,
    "speed": Slider(
        label="Speed of Boids",
        value=5,
        min=1,
        max=20,
        step=1,
    ),
    "vision": Slider(
        label="Vision of Bird (radius)",
        value=10,
        min=1,
        max=50,
        step=1,
    ),
    "separation": Slider(
        label="Minimum Separation",
        value=2,
        min=1,
        max=20,
        step=1,
    ),
}

model = BoidFlockers()

page = SolaraViz(
    model,
    components=[make_space_component(agent_portrayal=agent_portrayal, backend="matplotlib")],
    model_params=model_params,
    name="Boid Flocking Model",
)
page
