from questionManager import selectRandomWord, selectRandomCharacters



def startGame(Game):
    i = 0

    print('Starting game.')
    
    while Game.getGameStatus() == "playing":
        if i >= len(Game.getPlayers()):
            i = 0

        player_in_turn = Game.getPlayers()[i]

        print('Sending question')
        

        chars = selectRandomCharacters( selectRandomWord(dictionary) )
        

        valid_responses = getValidResponses(chars)


        
        response = input(f'Escribe una palabra que contenga {chars}: ')

        
        if response in valid_responses:
            player_in_turn.setPoint(1)
            print(player_in_turn.getPoints())

        else:
            if player_in_turn.setLifes() == 0:
                Game.setGameStatus('finished')
            
        i++
