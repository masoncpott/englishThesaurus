import json
from difflib import get_close_matches

# put the json data into an dictionary of key:value pairs
data = json.load(open('data.json'))

# create a function that takes a word (str) and returns the definition of that word
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        return input("Did you mean: %s instead?" % get_close_matches(word, data.keys(), cutoff=0.8)[0])
    else:
        return "Definition could not be found."

search_term = input("Please enter a word: ")

print(translate(search_term))