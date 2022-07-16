#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""  Perform Character Level Tokenization  """


import pprint
import logging

from deepnlu.services.tokenizer.dto import d_currency


class CharacterLevelTokenizer(object):
    """  Perform Character Level Tokenization  """

    def __init__(self,
                 input_text: str):
        """
        Created:
            29-Sept-2021
            craig@graffl.ai
        :param input_text:
        """
        self._input_text = input_text
        self._currency_symbols = list(d_currency.keys())

    def _is_punctuation(self,
                        ch: str,
                        p2: str or None,
                        p1: str or None,
                        n1: str or None,
                        n2: str or None) -> bool:
        if ch == '.' and p1 and p1.isupper():
            return False
        if ch == '.' and p1 and p1.isalpha() and p2 and p2 == '.':
            return False
        if ch == '.' and n1 and n1.isalpha() and n2 and n2 == '.':
            return False
        if ch == '-':
            return False
        if ch == ' ':
            return True
        if ch == '"':
            return True
        if ch == '_':
            return False
        if ch == ',' and p1 and p1.isdigit() and n1 and n1.isdigit():
            return False
        if ch in self._currency_symbols:
            return True
        if ch.isdigit():
            return False
        if ch.isnumeric():
            return False
        if ch.isalpha():
            return False
        return True

    def _mask_input(self) -> list:

        i = 0
        mask = []
        len_of_text = len(self._input_text)

        while i < len_of_text:

            def _prior(position: int) -> str or None:
                if i - position >= 0:
                    return self._input_text[i - position]

            def _next(position: int) -> str or None:
                if i + position < len_of_text:
                    return self._input_text[i + position]

            mask.append(
                self._is_punctuation(
                    ch=self._input_text[i],
                    p2=_prior(2),
                    p1=_prior(1),
                    n1=_next(1),
                    n2=_next(2)))

            i += 1

        return mask

    def _apply_mask(self,
                    mask: list) -> list:
        buffer = []
        master = []

        is_break = False
        is_continuous = False

        len_of_mask = len(mask)
        for i in range(0, len_of_mask):

            if mask[i]:

                if len(buffer):
                    master.append(buffer)

                master.append([mask[i]])
                buffer = []

            else:
                buffer.append(mask[i])

        if len(buffer):
            master.append(buffer)

        return master

    def _tokenize(self,
                  master: list) -> dict:

        ctr = 0
        d_tokens = {}

        original_buffer = []
        token_buffer = []

        for i in range(0, len(master)):
            buffer = master[i]

            for j in range(0, len(buffer)):
                mask = buffer[j]

                if not mask:
                    token_buffer.append(self._input_text[ctr])

                original_buffer.append(self._input_text[ctr])
                ctr += 1

            if not len(''.join(original_buffer).strip()):
                original_buffer = []
                continue

            s_original = ''.join(original_buffer)
            s_normalized = ''.join(token_buffer)
            s_normalized = s_normalized.replace('-', ' ')

            if not len(s_normalized):  # spaCy doesn't like blanks
                s_normalized = s_original

            d_tokens[i] = {
                "original": s_original,
                "normalized": s_normalized}

            original_buffer = []
            token_buffer = []

        return d_tokens

    def _post_process(self,
                      d_tokens: dict) -> dict:
        """ Primarily Designed to Handle Repeating Punctuation as a single term """

        normalized = []
        tokens = [d_tokens[x] for x in d_tokens]

        i = 0
        num_of_tokens = len(tokens)

        while i < num_of_tokens:
            buffer = []

            def _next() -> str or None:
                if i + 1 < num_of_tokens:
                    return tokens[i + 1]['original']

            t_next = _next()
            t_curr = tokens[i]['original']

            is_punct = self._is_punctuation(ch=t_curr,
                                            p2=None,
                                            p1=None,
                                            n1=t_next,
                                            n2=None)
            is_single_repeating = len(t_curr) == 1 and \
                t_next and \
                t_curr == t_next

            if is_punct and is_single_repeating:
                buffer.append(tokens[i])
                i += 1

                while i + 1 < num_of_tokens and tokens[i]['original'] == tokens[i+1]['original']:
                    buffer.append(tokens[i])
                    i += 1

                buffer.append(tokens[i])
                normalized.append(buffer)

            else:
                normalized.append([tokens[i]])

            i += 1

        ctr = 0
        d_normal = {}

        for item in normalized:
            if len(item) == 1:
                d_normal[ctr] = item[0]
            else:
                text = ''.join(x['original'] for x in item).strip()
                if len(text):
                    d_normal[ctr] = {
                        'normalized': text[0],
                        'original': text}

            ctr += 1

        return d_normal

    def process(self) -> dict:

        # Step 1: Mask the Input
        mask = self._mask_input()

        # Step 2: Apply the Mask
        master = self._apply_mask(mask)

        # Step 3: Tokenize the Input
        d_tokens = self._tokenize(master)

        # Step 4: Post Process the Tokens
        d_tokens = self._post_process(d_tokens)

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Character Level Tokenization Complete",
                f"\tInput Text: {self._input_text}",
                pprint.pformat(d_tokens)]))

        return d_tokens
