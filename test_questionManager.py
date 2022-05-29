from questionManager import selectRandomWord, selectRandomCharacters
import pytest
import json


DICTIONARY = []

with open('./static/dictionary_es.json') as json_data:
    DICTIONARY = json.load(json_data) 


TEST_WORD = selectRandomWord(DICTIONARY)

def test_selectRandomWord():
    assert ( type(TEST_WORD) is str ) and ( len(TEST_WORD) >= 3)

def test_RandomCharacters():
    char = selectRandomCharacters(TEST_WORD) 
    assert ( type(char) is str ) and ( len(char) <= 3)

 
