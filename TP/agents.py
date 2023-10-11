from mesa import Agent


# Define agent classes
class Token(Agent):
    def __init__(self, unique_id, x, y, model):
        super().__init__(unique_id, model)
        # EV attributes
        self.type = "Resource"
        self.charge_rate = 0
        self.pos = (x,y)
        self.holder = None

    def step(self):
        # Implement Token behavior here
        pass

class Player(Agent):
    def __init__(self, unique_id, model, playertype):
        super().__init__(unique_id, model)
        # Player attributes
        self.type = playertype
        self.score = 0
        self.deck = []

    def place_house(self) -> None:
        pass

    def receive_profit(self) -> None:
        pass

    def consult_player(self, ally) -> None: 
        pass

    def house_decide_location(self) -> None:
        pass

    def step(self):
        # Implement Player behavior here
        self.receive_profit()
        pass

class Card(Agent):
    def __init__(self, x, y, model):
        super().__init__(x, y, model)

    def step(self):
        # Implement Card behavior here
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
