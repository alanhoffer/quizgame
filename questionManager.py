import random
import json

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


def getValidResponses(chars, dictionary):
    valid_responses = []

    for word in dictionary:
        if chars in word:
            valid_responses.append(word)

    return valid_responses

def loadDictionary():
    with open('./static/dictionary_es.json') as json_data:
        DICTIONARY = json.load(json_data)
        return DICTIONARY
