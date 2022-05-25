from mutato import __version__


import os
from pprint import pprint

from datablock import FindNER
from datablock import FindSynonyms

from mutato.dmo import ExactMatchSwapper


candidate_tokens = [
    [
        {'dep': 'advmod',
         'ent': '',
         'head': '2#5#2158845516055552166',
         'id': '0#0#16331095434822636218',
         'is_alpha': True,
         'is_punct': False,
         'is_stop': True,
         'is_wordnet': True,
         'normal': 'how',
         'noun_number': '',
         'pos': 'ADV',
         'sentiment': 0.0,
         'shape': 'xxx',
         'stem': 'how',
         'tag': 'WRB',
         'tense': '',
         'text': 'how ',
         'verb_form': '',
                      'x': 0,
                      'y': 3},
        {'dep': 'ROOT',
         'ent': '',
         'head': '2#5#2158845516055552166',
         'id': '2#5#2158845516055552166',
         'is_alpha': True,
         'is_punct': False,
         'is_stop': True,
         'is_wordnet': True,
         'normal': 'do',
         'noun_number': '',
         'pos': 'VERB',
         'sentiment': 0.0,
         'shape': 'xx',
         'stem': 'do',
         'tag': 'VBP',
         'tense': 'pres',
         'text': 'do ',
         'verb_form': 'fin',
                      'x': 4,
                      'y': 6},
        {'dep': 'nsubj',
         'ent': '',
         'head': '6#14#2158845516055552166',
         'id': '4#9#7624161793554793053',
         'is_alpha': True,
         'is_punct': False,
         'is_stop': True,
         'is_wordnet': True,
         'normal': 'you',
         'noun_number': '',
         'pos': 'PRON',
         'sentiment': 0.0,
         'shape': 'xxx',
         'stem': 'you',
         'tag': 'PRP',
         'tense': '',
         'text': 'you ',
         'verb_form': '',
                      'x': 7,
                      'y': 10},
        {'dep': 'ROOT',
         'ent': '',
         'head': '6#14#2158845516055552166',
         'id': '6#14#2158845516055552166',
         'is_alpha': True,
         'is_punct': False,
         'is_stop': True,
         'is_wordnet': True,
         'normal': 'do',
         'noun_number': '',
         'pos': 'VERB',
         'sentiment': 0.0,
         'shape': 'xx',
         'stem': 'do',
         'tag': 'VBP',
         'tense': 'pres',
         'text': 'do',
         'verb_form': 'fin',
                      'x': 11,
                      'y': 13}]]


def test_component():

    ont14n = 'chitchat'

    ner_finder = FindNER(ont14n)
    syn_finder = FindSynonyms(ont14n)

    dmo = ExactMatchSwapper(ner_finder=ner_finder,
                            syn_finder=syn_finder,
                            ontologies=[ont14n])

    # assert dmo

    # result = dmo.process(candidate_tokens)
    # assert result

    # pprint(result)


def main():
    test_component()


if __name__ == "__main__":
    main()
