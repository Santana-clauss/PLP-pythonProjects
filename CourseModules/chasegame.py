import random

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self):
        self.position += random.randint(-1, 1)

class ChaseGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        while abs(self.player1.position - self.player2.position) > 3:
            self.player1.move()
            self.player2.move()

        if self.player1.position > self.player2.position:
            print(f"{self.player1.name} caught {self.player2.name}!")
        else:
            print(f"{self.player2.name} caught {self.player1.name}!")

player1 = Player("Player 1", 0)
player2 = Player("Player 2", 10)

game = ChaseGame(player1, player2)
game.play()
