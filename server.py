from mesa.visualization.modules import CanvasHexGrid
from mesa.visualization.ModularVisualization import ModularServer

from TP.agents import Token, Player, Card, Gamemaster
from TP.model import TippingPointModel
import TP.config as cfg


# Define the visualization
def agent_portrayal(agent):
    portrayal = {"Shape": "hexagon",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "black",
                 "r": 1}
    if isinstance(agent, Token):
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1
    elif isinstance(agent, Player):
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 2
    elif isinstance(agent, Card):
        portrayal["Color"] = "green"
        portrayal["Layer"] = 3
    elif isinstance(agent, Gamemaster):
        portrayal["Color"] = "yellow"
        portrayal["Layer"] = 4
    return portrayal

# Create and run the model
model = TippingPointModel(cfg.grid_width, cfg.grid_height, cfg.hex_radius)

# Create a hex grid visualization
canvas_element = CanvasHexGrid(agent_portrayal, cfg.grid_width, cfg.grid_height, cfg.hex_radius, 500, 500)

# Create the server and run the model
server = ModularServer(TippingPointModel, 
                       [canvas_element], 
                       "Hexagonal Model", 
                       {"width": cfg.grid_width, 
                        "height": cfg.grid_height, 
                        "hex_radius": cfg.hex_radius,
                        })
server.port = 8521
server.launch()
