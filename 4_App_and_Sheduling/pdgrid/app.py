from model import PDModel
from mesa.visualization import (
    Slider,
    SolaraViz,
    make_plot_component,
    make_space_component,
)
from mesa.visualization.components import AgentPortrayalStyle

## Define agent portrayal (color as function of cooperation, shape, size
def agent_portrayal(agent):
    return AgentPortrayalStyle(
        color = "blue" if agent.move == "C" else "red",
        marker= "s",
        size= 40,
    )

## List model aprameters: seed, grid size, activation regime
model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "width": Slider("Grid Width", value=40, min=10, max=100, step=1),
    "height": Slider("Grid Height", value=40, min=10, max=100, step=1),
    "order": {
        "type": "Select",
        "value": "Simultaneous",
        "values": PDModel.activation_regimes,
        "label": "Activation Order",
    },
}
## Define spatial visualization
SpaceGraph = make_space_component(agent_portrayal=agent_portrayal, draw_grid=False)
## Define plot of cooperation over time
CoopPlot = make_plot_component("Cooperators")
## Instantiate model
pd_model = PDModel()
## Define page components
page = SolaraViz(
    model=pd_model,
    components=[SpaceGraph, CoopPlot],
    model_params=model_params,
    name="Demographic Prisoner's Dilemma",
)
## Return page
page
