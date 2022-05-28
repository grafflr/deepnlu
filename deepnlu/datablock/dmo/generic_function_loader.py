# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Function Loader using Reflection """


import os
import logging
import importlib.util

from baseblock import EnvIO
from baseblock import FileIO
from baseblock import Enforcer
from baseblock import Stopwatch
from baseblock import BaseObject


class GenericFunctionLoader(BaseObject):
    """ Generic Function Loader using Reflection """

    def __init__(self,
                 subdir: str):
        """
        Created:
            11-Oct-2021
            craig@grafflr.ai
            *   refactored out of 'find-lookup' in pursuit of
                https://github.com/grafflr/graffl-core/issues/30#issuecomment-940252993
        """
        BaseObject.__init__(self, __name__)
        self._subdir = subdir

    def _inputdir(self) -> str:

        path = os.path.normpath(os.path.join(
            EnvIO.str_or_exception('GRAFFLR_HOME'),
            self._subdir))

        FileIO.exists_or_error(path)

        return path

    def load(self,
             module_name: str):

        sw = Stopwatch()

        inputdir = self._inputdir()
        class_name = f"{module_name}"
        module_name = f"{module_name}.py"

        def module_loader() -> object:

            file_name = os.path.join(
                inputdir, module_name)

            spec = importlib.util.spec_from_file_location(
                class_name, file_name)

            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)

            klass = getattr(foo, class_name)

            return klass

        finder = module_loader()

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Loaded Function",
                f"\tModule Name: {module_name}",
                f"\tTotal Time: {str(sw)}"]))

        return finder
