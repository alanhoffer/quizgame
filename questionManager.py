import random

def selectRandomWord(dictionary):
    if ( (type(dictionary) is list) and (len(dictionary) > 1) ):
        rnumber = random.randint(0, len(dictionary))
        return dictionary[rnumber]
    else:
        raise TypeError('The variable that was passed is not fine my bro')


def selectRandomCharacters(word):
    

    if (type(word) is str) and (len(word) >= 3):
        rcharacter_length = random.randint(2,3)
        character_position = random.randint(0, len(word)-3)
        character = ""

        for i in range(rcharacter_length):
            character = character + word[character_position]
            character_position += 1
        return character
    else:
        raise TypeError('The variable that was passed is not a str or is to short')



print(selectRandomCharacters("motivacion"))

