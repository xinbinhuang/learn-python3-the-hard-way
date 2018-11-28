DIRECTIONS = ['north', 'south', 'east', 'west',
              'down', 'up', 'left', 'right', 'back']
VERBS = ['go', 'stop', 'kill', 'eat']
STOPS = ['the', 'in', 'of', 'from', 'at', 'it']
NOUNS = ['door', 'bear', 'princess', 'cabinet']


def scan(words):

    lexicon_map = {'direction': DIRECTIONS,
                   'verb': VERBS,
                   'stop': STOPS,
                   'noun': NOUNS}

    word_lst = words.split()
    sentence = []
    for word in word_lst:
        word_lower = word.lower()

        # loop through all the lexicons
        for lex_type, lex in lexicon_map.items():
            if word_lower in lex:
                lex_tuple = (lex_type, word)
                sentence.append(lex_tuple)
                break
        # if not found in lexicons, try convert to numbers or output error word
        else:
            try:
                word = ('number', int(word))
            except ValueError:
                word = ('error', word)

            sentence.append(word)

    return sentence
