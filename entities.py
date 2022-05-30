
class Game():
    def __init__(self, id=0, players=[], status=""):
        self.id = id
        self.players = players
        self.status = status
    
    def addPlayer(self, player):
        try:
            self.players.append(player)
        except:
            print(f'Error adding player {str(player.id)}  to game {str(self.gameid)}')

    def setGameStatus(self, status):
        try:
            self.status = status
        except:
            print(f'Error changing the game status {str(self.status)} to {str(status)} ')

    def getPlayers(self):
        return self.players

    def getGameStatus(self):
        return self.status








class Player():
    def __init__(self, id=0, name="", gameid=0, points=0, lifes=0,  status=""):
        self.id = id
        self.name = name
        self.gameid = gameid
        self.points = points
        self.lifes = lifes
        self.status = status


    def resetLifes(self):
        self.lifes = 2
        self.points = 0

    def setPoint(self, quantity):
        try:
            self.points += quantity
        except:
            print('Error adding points to player:', self.id)

    def setStatus(self, status):
        try:
            self.status = status
        except:
            print(f'Error changing player {str(self.id)} status')

    def setGameid(self, gameid):
        try:
            self.gameid = gameid
        except:
            print(f'Error adding player {str(self.id)} to game {str(gameid)}')

    
    def setLifes(self, quantity=1):
        self.lifes -= quantity
        return self.lifes

    def getPoints(self):
        return self.points

    
    def getLifes(self):
        return self.lifes




