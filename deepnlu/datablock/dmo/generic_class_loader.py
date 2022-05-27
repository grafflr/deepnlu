# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generic Class Loader using Reflection """


import os
import logging
import importlib.util

from baseblock import EnvIO
from baseblock import FileIO
from baseblock import Stopwatch
from baseblock import BaseObject


class GenericClassLoader(BaseObject):
    """ Generic Class Loader using Reflection """

    def __init__(self):
        """
        Created:
            11-Oct-2021
            craig@grafflr.ai
            *   refactored out of 'find-lookup' in pursuit of
                https://github.com/grafflr/graffl-core/issues/30#issuecomment-940252993
        """
        BaseObject.__init__(self, __name__)

    def load(self,
             class_suffix: str,
             module_suffix: str,
             package_name: str):

        sw = Stopwatch()

        def file_path() -> str:
            file_path = os.path.normpath(os.path.join(
                os.getcwd(),
                'deepnlu/datablock/os/owl',
                package_name))

            FileIO.exists_or_error(file_path)

            return file_path

        file_path = file_path()
        class_name = f"{package_name.title()}{class_suffix}"
        module_name = f"{package_name}_{module_suffix}.py"

        def module_loader() -> object:

            file_name = os.path.join(
                file_path, module_name)

            spec = importlib.util.spec_from_file_location(
                class_name, file_name)

            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)

            klass = getattr(foo, class_name)

            return klass()

        finder = module_loader()

        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug('\n'.join([
                "Loaded Class",
                f"\tPackage Name: {package_name}",
                f"\tTotal Time: {str(sw)}"]))

        return finder
