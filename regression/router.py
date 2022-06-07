#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Regression Router """


from regression import RegressionAPI


def run() -> None:
    api = RegressionAPI()
    assert api

    api.process()


def main():
    run()


if __name__ == "__main__":
    main()
