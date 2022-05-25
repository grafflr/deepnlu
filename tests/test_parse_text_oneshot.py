# -*- coding: UTF-8 -*-
import pprint


from deepnlu.svc import ParseTextOneShot


def test_service():

    svc = ParseTextOneShot(['nursing'])
    assert svc

    svcresult = svc.process("registered nurse")
    assert svcresult


def main():
    test_service()


if __name__ == "__main__":
    main()
