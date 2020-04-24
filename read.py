from nltk.tokenize import sent_tokenize
import random

def get_tweet():
    file = 'life.txt'

    with open(file) as f:
        text = f.readlines()[79:3149]
        text = ''.join(text)
        text = text.replace('\n', ' ')
        sentences = sent_tokenize(text)
        length = len(sentences)

        sentence_to_print = ''
        while sentence_to_print == '': 
            sentence_number = random.randint(0, length)
            sentence_length = len(sentences[sentence_number])
            if sentence_length < 180 and sentence_length > 21:
                sentence_to_print = sentences[sentence_number]

    return sentence_to_print



