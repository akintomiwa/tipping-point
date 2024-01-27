from mesa import Agent
from random import choice


# Define agent classes
# class Token(Agent):
#     def __init__(self, unique_id, x, y, model):
#         super().__init__(unique_id, model)
#         # EV attributes
#         self.type = "Resource"
#         self.charge_rate = 0
#         self.pos = (x,y)
#         self.holder = None

#     def step(self):
#         # Implement Token behavior here
#         pass

class Player(Agent):
    def __init__(self, unique_id, model, playertype):
        super().__init__(unique_id, model)
        # Player attributes
        self.type = playertype
        self.score = 0
        self.deck = []

    def select_token_from_deck(self):
        # randomly select token from deck
        selected = choice(self.deck)
        return selected

    def place_house_token(self, token) -> None:
        # place house on random grid location 
        target = self.model.grid.random
        pass

    def receive_profit(self,token) -> int:
        self.score += token.value
        return self.score
        pass

    def consult_player(self, teammate) -> None: 
        pass

    # def house_decide_location(self) -> None:
    #     pass

    def step(self):
        # Implement Player behavior here
        self.receive_profit()
        pass


# Primitives
# Token, SmallResourceToken, LargeResourceToken, SmallWasteToken, SmallWasteToken, LargeHouseToken, SmallHouseToken, 

class Token(Agent):
    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        # token attr 
        self.type = None
        self.value = None
        self.pos = (x,y)
        self.holder = None

    def step(self):
        # Implement Token behavior here
        pass

class SmallResourceToken(Token):
    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        # token attr 
        self.type = "Resource"
        self.value = 1

    def step(self):
        # Implement Token behavior here
        pass

class LargeResourceToken(Token):
    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        # token attr 
        self.type = "Resource"
        self.value = 3

    def step(self):
        # Implement Token behavior here
        pass

class Gamemaster(Agent):
    def __init__(self, x, y, model):
        super().__init__(x, y, model)

        self.deck = []

    def give_token(self, recipient:Player)-> None:
        token = self.deck.pop(0)
        recipient.deck.append(token)
        pass
    
    def give_card(self, recipient:Player)-> None:
        token = self.deck.pop(0)
        recipient.deck.append(token)
        pass

    def step(self):
        # Implement Gamemaster behavior here
        pass
