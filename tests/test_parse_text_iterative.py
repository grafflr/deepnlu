# -*- coding: UTF-8 -*-


from pprint import pprint


from deepnlu.recipe.svc import ParseTextIterative


def test_process_input_text_1():

    input_text = "please generate something similar to 'consistently achieves timely delivery'"
    assert type(input_text) == str

    svc = ParseTextIterative(['appraisal', 'ontologica'])
    assert svc

    svc.process(input_text)
    svc.process(input_text)
    svc.process(input_text)
    svc.process(input_text)
    svc.process(input_text)
    svc.process(input_text)
    svc.process(input_text)
    svc.process(input_text)

    svcresult = svc.process(input_text)
    assert svcresult

    pprint(svcresult)


def test_process_input_text_2():

    input_text = """As a Distinguished Engineer and IBM Executive Leader, I transform people, companies, and lives through analytics and empowerment with data. 
    As a consummate advocate for responsible stewardship of data and science, I infuse diversity into global and corporate leadership and drive human-centered design into cognitive enterprises. 
    As a global leader and influencer, I develop and lead teams of data scientists, data engineers, data architects, data analysts and consultants who develop and deploy AI solutions for IBM's clients. 
    My current role is to transform the world's largest IT Shop, GTS, through the application of AI and Cognitive Science. I bind my background and training in anthropology, language and data science to develop models for the cultural transformation of our ~100k strong workforce. I measure my success by the adoption of my models and seek every opportunity to develop our humans. 
    Beth inspires and leads large, geographically dispersed analytic teams to develop and deliver cognitive analytic solutions that deliver actionable insights for IBM's clients."""
    assert type(input_text) == str

    svc = ParseTextIterative(['appraisal'])
    assert svc

    svcresult = svc.process(input_text, 1)
    assert svcresult

    pprint(svcresult)


def main():
    test_process_input_text_1()
    test_process_input_text_2()


if __name__ == "__main__":
    main()
