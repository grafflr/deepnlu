
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# pylint:disable=bad-whitespace
# pylint:disable=line-too-long
# pylint:disable=too-many-lines
# pylint:disable=invalid-name

# #########################################################
#
#       ************** !! WARNING !! ***************
#       ******* THIS FILE WAS AUTO-GENERATED *******
#       ********* DO NOT MODIFY THIS FILE **********
#
# #########################################################

class ChitchatTemplateConstraints(object):

    @staticmethod
    def prov() -> dict:
        return {
 'action': ['router.py',
            'plac_core.py',
            'owl2py_orchestrator.py',
            'generate_runtime_dictionaries.py',
            'generate_runtime_dictionary.py',
            'owl_data_load_dict.py',
            'common_utils.py'],
 'config': {'classname': 'ChitchatTemplateConstraints',
            'filename': 'chitchat_template_constraints',
            'queries': ['templates.sparql'],
            'transformers': ['template_constraints', 'sentence_transform']},
 'source': 'chitchat.owl',
 'time': '2022-04-27 21:17:15.094355'}

    __data = {
    'i like them all but i really like {animal}': [   'I Like Them All But I '
                                                      'Really Like Kitties',
                                                      'I Like Them All But I '
                                                      'Really Like Kittens',
                                                      'I Like Them All But I '
                                                      'Really Like Puppies',
                                                      'I Like Them All But I '
                                                      'Really Like Ocelots',
                                                      'I Like Them All But I '
                                                      'Really Like Horsies',
                                                      'I Like Them All But I '
                                                      'Really Like Doggies',
                                                      'I Like Them All But I '
                                                      'Really Like Horses',
                                                      'I Like Them All But I '
                                                      'Really Like Otters',
                                                      'I Like Them All But I '
                                                      'Really Like Cats',
                                                      'I Like Them All But I '
                                                      'Really Like Dogs'],
    'my favorite animal is {animal}': [   'My Favorite Animal Is an Ocelot',
                                          'My Favorite Animal Is an Animal',
                                          'My Favorite Animal Is an Otter',
                                          'My Favorite Animal Is a Kitten',
                                          'My Favorite Animal Is a Horse',
                                          'My Favorite Animal Is a Puppy',
                                          'My Favorite Animal Is a Cat',
                                          'My Favorite Animal Is a Dog'],
    'my favorite are {animal}': [   'My Favorite Are Kitties',
                                    'My Favorite Are Horsies',
                                    'My Favorite Are Kittens',
                                    'My Favorite Are Ocelots',
                                    'My Favorite Are Puppies',
                                    'My Favorite Are Doggies',
                                    'My Favorite Are Otters',
                                    'My Favorite Are Horses',
                                    'My Favorite Are Dogs',
                                    'My Favorite Are Cats']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
