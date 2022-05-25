#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" deepNLU Orchestrator """


import os
import plac

from deepnlu import DeepNluAPI


def main():

    input_dir = "c:/Users/Craig/Desktop/input"
    output_dir = "c:/Users/Craig/Desktop/output"

    api = DeepNluAPI()

    input_files = api.load_files(input_dir)
    api.run(input_files, output_dir)


if __name__ == "__main__":
    plac.call(main)
