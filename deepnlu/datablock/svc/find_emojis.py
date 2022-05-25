# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Facade to interact with Emojis """


from random import sample
from functools import lru_cache

from baseblock import BaseObject

from datablock.os.emojis import emojis


class FindEmojis(BaseObject):
    """ Generic Facade to interact with Emojis """

    __slots__ = (
    )

    def __init__(self):
        """
        Created:
            10-Mar-2022
            craig@grafflr.ai
            *   https://github.com/grafflr/graffl-core/issues/216
        """
        BaseObject.__init__(self, __name__)
        self._emojis = emojis

    def all(self) -> list:
        return self._emojis

    def exists(self,
               input_text: str) -> bool:
        if ' ' in input_text:
            input_text = input_text.replace(' ', '_')
        return input_text.strip().lower() in self.all()

    def random(self,
               funny: int = None,
               positive: int = None) -> str:

        def _funny() -> set:
            result = self.by_funny_level(funny)
            if result:
                return set(result)
            return set()

        def _positive() -> set:
            result = self.by_positive_level(positive)
            if result:
                return set(result)
            return set()

        if funny and positive:
            result = _funny().intersection(_positive())
            if result and len(result):
                return sample(result, 1)[0]

        elif funny:
            result = _funny()
            if len(result):
                return sample(result, 1)[0]

        elif positive:
            result = _positive()
            if len(result):
                return sample(result, 1)[0]

        return sample(self.all(), 1)[0]

    @lru_cache
    def by_cluster(self,
                   cluster: int) -> list or None:
        """ a Cluster is an integer value 
            two emojis with identical cluster values are similar

        Example:
            :see_no_evil: shares a cluster with :speak_no_evil:

        Args:
            cluster (int): a cluster number

        Returns:
            list or None: a list of similar emojis (if any)
        """
        from datablock.os.emojis import d_emoji_cluster_fwd

        if cluster in d_emoji_cluster_fwd:
            return d_emoji_cluster_fwd[cluster]

    @lru_cache
    def in_same_cluster(self,
                        emoji_name: str) -> list or None:
        """ Find the Emojis in the same Cluster

        Args:
            emoji_name (str): the short code of the emoji to search on

        Returns:
            list or None: a list of similar emojis (if any)
        """
        from datablock.os.emojis import d_emoji_cluster_rev

        emoji_name = emoji_name.lower().strip()
        if emoji_name not in d_emoji_cluster_rev:
            return None

        master = set()
        rev_results = d_emoji_cluster_rev[emoji_name]

        if rev_results:
            for rev_result in rev_results:
                [master.add(x) for x in self.by_cluster(rev_result)]

        master = [x for x in master if x != emoji_name]
        return sorted(master, key=len)

    @lru_cache
    def by_gender(self,
                  gender: str) -> list or None:
        """ Search for Emojis by Gender (M or F)

        Args:
            gender (str): M (Male), F (Female), U (Unknown)

        Returns:
            list or None: a list of emojis by gender
        """
        from datablock.os.emojis import d_emoji_gender_fwd

        gender = gender.lower().strip()
        if gender in d_emoji_gender_fwd:
            return d_emoji_gender_fwd[gender]

    @lru_cache
    def with_same_gender(self,
                         emoji_name: str) -> list or None:
        """ Find Emojis with the same gender

        Args:
            emoji_name (str): the short code of the emoji to search on

        Returns:
            list or None: a list of similar emojis (if any)
        """
        from datablock.os.emojis import d_emoji_gender_rev

        emoji_name = emoji_name.lower().strip()
        if emoji_name in d_emoji_gender_rev:

            gender = d_emoji_gender_rev[emoji_name][0].lower()
            results = self.by_gender(gender)
            if results:
                return [x for x in results if x != emoji_name]

    @lru_cache
    def by_funny_level(self,
                       level: int) -> list or None:
        """ Find Emojis by 'Funniness' level

        Args:
            level (int): Scaled 1-5
                1 = Rage
                2 = Sad
                3 = Neutral
                4 = Slightly Funny
                5 = Highly Funny

        Returns:
            list or None: a list of emojis by funniness level
        """
        from datablock.os.emojis import d_emoji_funny_fwd

        if level in d_emoji_funny_fwd:
            return d_emoji_funny_fwd[level]

    @lru_cache
    def just_as_funny(self,
                      emoji_name: str) -> list or None:
        """ Find Emojis that are just as funny

        Args:
            emoji_name (str): the short code of the emoji to search on

        Returns:
            list or None: a list of similar emojis (if any)
        """
        from datablock.os.emojis import d_emoji_funny_rev

        emoji_name = emoji_name.lower().strip()
        if emoji_name in d_emoji_funny_rev:
            master = set()

            rev_results = d_emoji_funny_rev[emoji_name]
            if rev_results:
                for rev_result in rev_results:
                    [master.add(x) for x in self.by_funny_level(rev_result)]

            master = [x for x in master if x != emoji_name]

            return sorted(master, key=len)

    @lru_cache
    def funnier(self,
                emoji_name: str) -> list or None:
        """ Find Emojis that are even funnier than the current one

        Args:
            emoji_name (str): the short code of the emoji to search on

        Returns:
            list or None: a list of funnier emojis (if any)
        """
        from datablock.os.emojis import d_emoji_funny_rev

        emoji_name = emoji_name.lower().strip()
        if emoji_name in d_emoji_funny_rev:
            level = d_emoji_funny_rev[emoji_name][0]
            if level:
                results = self.by_funny_level(level + 1)
                if results:
                    return [x for x in results if x != emoji_name]

    @lru_cache
    def ironic_emojis(self) -> list or None:
        """ Return all emojis that could be ironic (in a given context)

        Returns:
            list or None: all known 'ironic' emojis
        """
        from datablock.os.emojis import emoji_ironic

        return emoji_ironic

    @lru_cache
    def random_ironic_emoji(self) -> str:
        return sample(self.ironic_emojis(), 1)[0]

    @lru_cache
    def by_positive_level(self,
                          level: int) -> list or None:
        """ Find Emojis by 'Positive' level

        Args:
            level (int): Scaled 1-5
                1 = Very Negative
                2 = Somewhat Negative
                3 = Neutral
                4 = Somewhat Positive
                5 = Very Positive

        Returns:
            list or None: a list of emojis by positive level
        """
        from datablock.os.emojis import d_emoji_positive_fwd

        if level in d_emoji_positive_fwd:
            return d_emoji_positive_fwd[level]

    @lru_cache
    def just_as_positive(self,
                         emoji_name: str) -> list or None:
        """ Find Emojis that are just as positive

        Args:
            emoji_name (str): the short code of the emoji to search on

        Returns:
            list or None: a list of similar emojis (if any)
        """
        from datablock.os.emojis import d_emoji_positive_rev

        emoji_name = emoji_name.lower().strip()
        if emoji_name in d_emoji_positive_rev:
            master = set()

            rev_results = d_emoji_positive_rev[emoji_name]
            if rev_results:
                for rev_result in rev_results:
                    [master.add(x) for x in self.by_positive_level(rev_result)]

            master = [x for x in master if x != emoji_name]

            return sorted(master, key=len)

    def faces(self) -> list:
        """ Return all emojis with ffaces

        Returns:
            list or None: all known 'face' emojis
        """
        from datablock.os.emojis import emoji_face

        return emoji_face

    def random_face(self) -> str:
        """ Return a random 'face' emoji

        Returns:
            str: a single random 'face' emoji
        """
        return sample(self.faces(), 1)[0]
