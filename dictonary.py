import json

#help(json.load)
data = json.load(open("data.json"))


def js(word):
    try:
        word = word.lower()
        if word in data:
           return data[word]
    
        else:
           return "The provided word is not exsist"

    except KeyError:
       return "Provided a meaningless input"

word = input("Enter the word:")


print(js(word))
