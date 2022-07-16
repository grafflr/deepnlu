#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Add Wordnet Flag to Token """


import pprint

from baseblock import BaseObject


class GrafflParserResultSet(BaseObject):
    """ Add Wordnet Flag to Token """

    def __init__(self):
        """
        Created:
            13-Oct-2021
            craig@graffl.ai
            *   refactored out of 'parse-input-tokens' in pursuit of
                https://github.com/grafflr/graffl-core/issues/41
        Updated:
            14-Oct-2021
            craig.@graffl.ai
            *   retokenize spaces back into owning tokens
                https://github.com/grafflr/graffl-core/issues/48#issuecomment-943793697
            *   ensure unique id and head values even when text is duplicated
                https://github.com/grafflr/graffl-core/issues/53#issuecomment-944001757
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                doc) -> list:
        """Transform spaCy doc into a result set

        Args:
            doc ([spacy]): a spaCy document

        Returns:
            list: a list of tokens
        """
        results = []

        i = 0

        tokens = [token for token in doc]
        while i < len(tokens):

            token = tokens[i]

            ## ---------------------------------------------------------- ##
            # Purpose:    Reclaim Whitespace into Prior Tokens
            # Reference:  https://github.com/grafflr/graffl-core/issues/48#issuecomment-944003662
            ## ---------------------------------------------------------- ##
            def has_trailing_space() -> bool:
                if i + 1 >= len(tokens):
                    return False
                return tokens[i + 1].text == ' '

            is_space_next = has_trailing_space()
            if is_space_next:
                i += 1

            def token_text() -> str:
                if is_space_next:
                    if not token.text.endswith(' '):
                        return f"{token.text} "
                return token.text

            ## ---------------------------------------------------------- ##
            # Purpose:    Ensure Unique IDs for duplicate text values
            # Reference:  https://github.com/grafflr/graffl-core/issues/53#issuecomment-944001757
            ## ---------------------------------------------------------- ##
            token_id = f"{token.i}#{token.idx}#{token.orth}"
            token_head = f"{token.head.i}#{token.head.idx}#{hash(token.head.orth)}"

            d_morph = token.morph.to_dict()

            def tense() -> str:
                if 'Tense' in d_morph:
                    return d_morph['Tense'].lower()
                return ''

            def number() -> str:
                """ Plural vs Singular vs None """
                if 'Number' in d_morph:
                    n = d_morph['Number']
                    if n == 'Sing':
                        return 'singular'
                    elif n == 'Plur':
                        return 'plural'
                    raise NotImplementedError(n)  # I want to know!
                return ''

            def verb_form() -> str:
                """  """
                if 'VerbForm' in d_morph:
                    return d_morph['VerbForm'].lower()
                return ''

            results.append({
                "id": token_id,
                "text": token_text(),
                "lemma": token.lemma_,
                "tense": tense(),  # Past vs Future
                "noun_number": number(),  # Singular vs Plural
                "verb_form": verb_form(),  # Gerund vs Infinitive etc
                "sentiment": token.sentiment,
                # "morph": token.morph.to_dict(),
                "pos": token.pos_,
                "tag": token.tag_,
                "dep": token.dep_,
                "ent": token.ent_type_,
                "shape": token.shape_,
                "head": token_head,
                "is_alpha": token.is_alpha,
                "is_stop": token.is_stop})

            i += 1

        return results
