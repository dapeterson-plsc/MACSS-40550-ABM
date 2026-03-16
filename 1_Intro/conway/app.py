import mesa
import numpy as np
from mesa.visualization import SolaraViz, make_space_component
from mesa.visualization.components import AgentPortrayalStyle

from model import ConwayModel

def agent_portrayal(agent):
    return AgentPortrayalStyle(
        color="white" if agent.state == 0 else "black",
        marker="s",
        size=100,
    )

def post_process(ax):
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "width": {
        "type": "SliderInt",
        "value": 20,
        "label": "Width",
        "min": 5,
        "max": 100,
        "step": 1,
    },
    "height": {
        "type": "SliderInt",
        "value": 20,
        "label": "Height",
        "min": 5,
        "max": 100,
        "step": 1,
    },
    "start_alive": {
        "type": "SliderFloat",
        "value": 0.3,
        "label": "Cells initially alive",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
}

conway_model = ConwayModel()

SpaceGraph = make_space_component(agent_portrayal, post_process=post_process, draw_grid=False)

page = SolaraViz(
    conway_model,
    components=[SpaceGraph],
    model_params=model_params,
    name="Game of Life",
)
page
