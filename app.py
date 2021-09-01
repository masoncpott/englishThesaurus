import json
from difflib import get_close_matches

# put the json data into an dictionary of key:value pairs
data = json.load(open('data.json'))

# create a function that takes a word (str) and returns the definition of that word
def translate(word):
    word = word.lower()
    titled_word = word.title()
    capped_word = word.upper()
    if word in data:
        return data[word]
    elif titled_word in data:
        return data[titled_word]
    elif capped_word in data:
        return data[capped_word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean: %s instead? Enter (y/n): " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        if yn =="y":
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif yn =="n":
            return "The word does not exist."
        else:
            return "We did not understand your search query."
    else:
        return "Definition could not be found."

search_term = input("Please enter a word: ")

output = translate(search_term)

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)