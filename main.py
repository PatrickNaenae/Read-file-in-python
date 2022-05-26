# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string

words = {}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        lines = f.read()
        lines = lines.translate(str.maketrans('', '', string.punctuation))
    return lines

def count_words():
    text = read_file_content("./story.txt").split()
    # [assignment] Add your code here
    for word in text:
        if word in words:
            words[word] = words[word] + 1
        else:
            words[word] = 1
    return words

countedWords = count_words()
print(countedWords)

