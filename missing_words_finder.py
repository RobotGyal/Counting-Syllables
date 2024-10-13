import sys 
from string import punctuation
import pprint
import json
from nltk.corpus import cmudict

cmudict = cmudict.dict()

def main():
    haiku = load_haiku('train.txt')
    exceptions = cmudict_missing(haiku)
    build_dict = input("\n Manaually build an exceptions dictionary (y/n)? \n")
    if build_dict.lower() == 'n':
        sys.exit()
    else:
        missing_words_dict = make_exceptions_dict(exceptions)
    save_exceptions(missing_words_dict)

def load_haiku(filename):
    """Open and return training corpus of haiku as a set."""
    with open(filename) as in_file:
        haiku = set(in_file.read().replace('-', '').split())
        return haiku

def cmudict_missing(word_set):
    """Find and return words in word set missing from cmudict."""
    exceptions = set()
    for word in word_set:
        word = word.lower().strip(punctuation)
        if word.endswith("s") or word.endswith("'s"):
            word = word[:2]
        if word not in cmudict:
            exceptions.add(word)
    print("\nexceptions:")
    print(*exceptions, sep='\n')
    print("\nNumber of unique words in haiku corpus = {}".format(len(word_set)))
    print("Number of words in corpus not in cmudict = {}".format(len(exceptions)))
    membership = (1-(len(exceptions) / len(word_set))) * 100
    print("cmudict membership = {:.1f}{}".format(membership, '%'))
    return exceptions

