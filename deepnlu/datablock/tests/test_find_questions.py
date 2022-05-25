

from baseblock import Stopwatch


def test_find_question():

    sw = Stopwatch()

    from datablock.svc import FindQuestions
    # print (f"1 - Perform Import: {str(sw)}")

    svc = FindQuestions()
    assert svc

    # print (f"2 - Initialize Service: {str(sw)}")

    for i in range(0, 10):
        result = svc.random()
        print(result)
        assert result

    print (f"3 - Make Calls: {str(sw)}")


def main():
    test_find_question()


if __name__ == "__main__":
    main()
