#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Graffl Tokenizer """


from deepnlu.datablock.svc import FindDictionaries


class TokenizeUseGraffl(object):
    """ Graffl Tokenizer """

    __acronym_delimiter = '~~'

    # __punkt = [
    #     '"',  # dquot
    #     "'",  # squot
    #     '!',  # exclamation point
    #     '?',  # question mark
    #     ",",  # comma
    #     ";",  # semicolon
    #     ":",  # colon
    # ]

    def __init__(self):
        """
        Created:
            29-Sept-2021
            craig@grafflr.ai
        Updated:
            14-Oct-2021
            craig@grafflr.ai
            *   added redelimit-spaces function
                https://github.com/grafflr/graffl-core/issues/48#issuecomment-943776908
        """
        pass

    def _replace_enclitics(self,
                           tokens: list) -> list:

        def transform(token: str) -> list:
            if "'" not in token:
                return [token]
            if token not in FindDictionaries.enclitics():
                return [token]
            return FindDictionaries.enclitics()[token]

        normalized = []
        for token in tokens:
            [normalized.append(x) for x in transform(token)]

        return normalized

    def _redelimit_acronyms(self,
                            tokens: list) -> list:

        def transform(token: str) -> str:
            if token.count('.') < 2:
                return token
            return token.replace('.', self.__acronym_delimiter)

        return [transform(x) for x in tokens]

    def _redelimit_abbreviations(self,
                                 tokens: list) -> list:

        def transform(token: str) -> str:
            if token not in FindDictionaries.abbreviations():
                return token
            return FindDictionaries.abbreviations()[token]

        return [transform(x) for x in tokens]

    def _undelimit_acronyms(self,
                            tokens: list) -> list:

        def transform(token: str) -> str:
            if self.__acronym_delimiter not in token:
                return token
            return token.replace(self.__acronym_delimiter, '.')

        return [transform(x) for x in tokens]

    def _handle_punkt(self,
                      tokens: list) -> list:

        def transform(token: str) -> list:

            if token.isalpha():
                return [token]

            master = []
            buffer = []

            prior_ch = None
            for ch in token:

                if ch.isalpha() or ch.isnumeric() or ch == ' ':
                    buffer.append(ch)
                elif ch in ['.', ','] and prior_ch and prior_ch.isnumeric():
                    buffer.append(ch)  # e.g., 1.06 or 325,000
                elif ch == "'" and prior_ch and prior_ch.isalpha():
                    buffer.append(ch)  # e.g., Women's
                else:
                    if len(buffer):
                        master.append(''.join(buffer))
                    if len(ch):
                        master.append(ch)
                    buffer = []

                prior_ch = ch

            if len(buffer):
                master.append(''.join(buffer))

            return master

        normalized = []
        for token in tokens:
            [normalized.append(x) for x in transform(token)]

        return normalized

    def _redelimit_spaces(self,
                          tokens: list) -> list:
        """Rejoin orphaned spaces with owning text

        Sample Input:
            ["health's ", 'management', ',', ' ', 'NPs']

        Sample Output
            ["health's ", 'management', ', ', 'NPs']

        Args:
            tokens (list): a list of tokens

        Returns:
            list: a normalized list of tokens
        """
        normalized = []

        i = 0
        while i < len(tokens):

            def next_token() -> str or None:
                if i + 1 < len(tokens):
                    return tokens[i + 1]

            t_curr = tokens[i]
            t_next = next_token()

            if t_next and t_next == ' ':
                normalized.append(f"{t_curr} ")
                i += 1
            else:
                normalized.append(t_curr)

            i += 1

        return normalized

    def _split(self,
               input_text: str) -> list:
        master = []

        buffer = []
        for ch in input_text:
            buffer.append(ch)
            if ch == ' ':
                master.append(''.join(buffer))
                buffer = []

        if len(buffer):
            master.append(''.join(buffer))

        return master

    def process(self,
                input_text: str) -> list:

        tokens = self._split(input_text)
        tokens = self._replace_enclitics(tokens)
        tokens = self._redelimit_acronyms(tokens)
        tokens = self._redelimit_abbreviations(tokens)
        tokens = self._handle_punkt(tokens)
        tokens = self._redelimit_spaces(tokens)
        tokens = self._undelimit_acronyms(tokens)

        return tokens
