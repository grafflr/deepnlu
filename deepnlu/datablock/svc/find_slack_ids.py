#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Find Slack Bot IDs """


from baseblock import BaseObject


class FindSlackIDs(BaseObject):
    """ Find Slack Bot IDs """

    __bot_ids = None
    __bot_names = None

    __johnbot_ids = [
        'U03E6GK9HK6'
    ]

    __d_bot_ids = {
        'U038QP8ND9P': 'Loqi',  # PROD instance
        'U03BYNQ68MP': 'Loqi',  # DEV instance
        'U030AJCKG3Z': 'Blattero',  # PROD instance
        'U03B5B9UXFZ': 'Blattero',  # DEV instance
        'U03E6GK9HK6': 'Johnbot'
    }

    def __init__(self):
        """ Change History:

        Created:
            4-May-2022
            craig@grafflr.ai
            *   in pursuit of
                https://github.com/grafflr/graffl-core/issues/304
        """
        BaseObject.__init__(self, __name__)

    def bot_ids(self) -> list:
        if not self.__bot_ids:
            self.__bot_ids = sorted(self.__d_bot_ids.keys())
        return self.__bot_ids

    def bot_names(self) -> list:
        if not self.__bot_names:
            self.__bot_names = sorted(self.__d_bot_ids.values())
        return self.__bot_names

    def name_by_id(self,
                   bot_id: str) -> str or None:
        if bot_id in self.__d_bot_ids:
            return self.__d_bot_ids[bot_id]
        return None

    def is_johnbot(self,
                   bot_id: str) -> bool:
        return bot_id in self.__johnbot_ids
