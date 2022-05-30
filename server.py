from game import startGame
from entities import Player, Game


newPlayer = Player(0, "", 0, 0, 2, "waiting")


newGame = Game(0, [newPlayer], "waiting")


newGame.setGameStatus("playing")

startGame(newGame)

