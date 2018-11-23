import random
import sys
from urllib.request import urlopen
from urllib.error import HTTPError

WORD_URL = "http://learncodethehardway.org/word.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
# if the url is failing open the local copy
try:
    file = urlopen(WORD_URL)
except HTTPError:
    file = open("data/words.txt", 'r')

for word in file.readlines():
    WORDS.append(str(word.strip()))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(", ".join(
            random.sample(WORDS, param_count)
        ))

    for sentence in snippet, phrase:
        result = sentence[:]
        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
