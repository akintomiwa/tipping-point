from mesa import Model
from mesa.time import RandomActivation
from mesa.space import HexGrid
from mesa.datacollection import DataCollector

import random
import logging
from TP.agents import Token, Player, Card, Gamemaster
import config as cfg

logger = logging.getLogger(__name__)

# Define the model class
class TippingPointModel(Model):
    def __init__(self, height, hex_radius, ticks):
        super().__init__()
        # init with input args
        self.running = True
        self.random = True
        self.ticks = cfg.num_rounds

        self.num_hexagons = cfg.grid_width * cfg.grid_height
        self.grid = HexGrid(cfg.grid_width, cfg.grid_height, cfg.hex_radius)
        self.schedule = RandomActivation(self)
        self.no_players = cfg.num_players

        # core structures 
        self.players = []
        self.deck = []
        
        # time 
        self._current_tick = 1


        # # Create and add agents to the model
        # for _ in range(cfg.num_tokens):  # Number of Tokens
        #     x, y = self.random_position()
        #     self.schedule.add(Token(x, y, self))

        for _ in range(cfg.num_players):  # Number of Players
            x, y = self.random_position()
            self.schedule.add(Player(x, y, self))

        for _ in range(cfg.num_cards):  # Number of Cards
            x, y = self.random_position()
            self.schedule.add(Card(x, y, self))

        self.schedule.add(Gamemaster(0, 0, self))

    def random_position(self):
        x = random.randint(-self.grid.width // 2, self.grid.width // 2)
        y = random.randint(-self.grid.height // 2, self.grid.height // 2)
        return x, y

    def step(self):
        self.schedule.step()
