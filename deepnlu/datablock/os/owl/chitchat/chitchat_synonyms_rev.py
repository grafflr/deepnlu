
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# pylint:disable=bad-whitespace
# pylint:disable=line-too-long
# pylint:disable=too-many-lines
# pylint:disable=invalid-name

# #########################################################
#
#       ************** !! WARNING !! ***************
#       ******* THIS FILE WAS AUTO-GENERATED *******
#       ********* DO NOT MODIFY THIS FILE **********
#
# #########################################################

class ChitchatSynonymsRev(object):

    @staticmethod
    def prov() -> dict:
        return {
 'action': ['router.py',
            'plac_core.py',
            'owl2py_orchestrator.py',
            'generate_runtime_dictionaries.py',
            'generate_runtime_dictionary.py',
            'owl_data_load_dict.py',
            'common_utils.py'],
 'config': {'classname': 'ChitchatSynonyms',
            'filename': 'chitchat_synonyms',
            'files': ['chitchat.txt'],
            'queries': ['synonyms.sparql'],
            'reverse': True,
            'transformers': ['lowercase', 'synonyms']},
 'source': 'chitchat.owl',
 'time': '2022-04-27 21:17:15.268855'}

    __data = {
    " i mean ... it happens, but that doesn't mean we have to like it": [   'sympathy_deflection'],
    '100': ['positive_slack_emoji'],
    'a fine day': ['good_weather_response'],
    'a fine day!': ['good_weather_response'],
    'ability action': ['ability_action'],
    'absolutely': ['agreeable_deflection'],
    'absolutely!': ['agreeable_deflection'],
    'action': ['action'],
    'adorkable': ['adorkable'],
    'adorkable response': ['adorkable_response'],
    'agreeable deflection': ['agreeable_deflection'],
    'animal': ['animal'],
    'animal slack emoji': ['animal_slack_emoji'],
    'are you busy': ['busy_state_action'],
    'are you busy?': ['busy_state_action'],
    'are you doing anything right now': ['free_state_action'],
    'are you doing anything right now?': ['free_state_action'],
    'are you free': ['free_state_action'],
    'bad weather': ['bad_weather'],
    'bad weather response': ['bad_weather_response'],
    'better than monday': ['friday_response'],
    'better than monday!': ['friday_response'],
    'big cat slack emoji': ['big_cat_slack_emoji'],
    'black_cat2': ['cat_slack_emoji'],
    'busy': ['busy_state_action'],
    'busy state action': ['busy_state_action'],
    'busy?': ['busy_state_action'],
    'but different': ['cliche_deflection'],
    'carousel_horse': ['horse_slack_emoji'],
    'case of the mondays': ['monday'],
    'cat': ['cat_slack_emoji', 'cat'],
    'cat slack emoji': ['cat_slack_emoji'],
    'cat2': ['cat_slack_emoji'],
    'cats': ['cat'],
    'cliche deflection': ['cliche_deflection'],
    'conditional state deflection': ['conditional_state_deflection'],
    'cry': ['negative_slack_emoji'],
    'crying_cat_face': ['negative_slack_emoji'],
    'deflection response': ['deflection_response'],
    'disagreeable deflection': ['disagreeable_deflection'],
    'dog': ['dog_slack_emoji', 'dog'],
    'dog slack emoji': ['dog_slack_emoji'],
    'dog2': ['dog_slack_emoji'],
    'doggies': ['dog'],
    'dogs': ['dog'],
    'doing great': ['state_greeting_response'],
    'doing just great': ['state_greeting_response'],
    'doing just great - thank you': ['state_greeting_response'],
    'doing just great - thank you!': ['state_greeting_response'],
    'doing real great': ['state_greeting_response'],
    'dude ... sorry': ['sympathy_deflection'],
    "dude i'm feeling that": ['sympathy_deflection'],
    'early': ['early'],
    'emoji': ['emoji'],
    'emotion': ['emotion'],
    'experience': ['experience'],
    'expressionless': ['neutral_slack_emoji'],
    'face_with_raised_eyebrow': ['insult_slack_emoji'],
    'face_with_rolling_eyes': ['negative_slack_emoji'],
    'favorable emotion': ['favorable_emotion'],
    'favorite animal response': ['favorite_animal_response'],
    'fine day': ['good_weather'],
    'fine weather': ['good_weather'],
    'fine, fine ... fine': ['state_greeting_response'],
    'fine, fine ... fine.': ['state_greeting_response'],
    'free state action': ['free_state_action'],
    'friday': ['friday'],
    'friday response': ['friday_response'],
    'geez ..': ['sympathy_deflection'],
    'geez ...': ['sympathy_deflection'],
    'general state action': ['general_state_action'],
    'good day': ['good_weather'],
    'good thanks': ['state_greeting_response'],
    'good thanks!': ['state_greeting_response'],
    'good weather': ['good_weather'],
    'good weather response': ['good_weather_response'],
    'great day': ['good_weather'],
    'great man': ['state_greeting_response'],
    'great weather': ['good_weather'],
    'greeting': ['greeting'],
    'greeting action': ['greeting_action'],
    'greeting response': ['greeting_response'],
    'greeting slack emoji': ['greeting_slack_emoji'],
    'grimacing': ['neutral_slack_emoji'],
    'guide_dog': ['dog_slack_emoji'],
    'handshake': ['greeting_slack_emoji'],
    'hanging in there': ['state_greeting_response'],
    'hanging in there.': ['state_greeting_response'],
    'happy friday': ['friday'],
    'happy monday': ['monday'],
    'hello': ['hello'],
    'hello response': ['hello_response'],
    'hello there': ['hello_response'],
    'hello there!': ['hello_response'],
    'hey': ['free_state_action'],
    'hey dude': ['state_greeting'],
    'hey whats up': ['state_greeting'],
    'hi': ['hello_response', 'hello'],
    'hi there': ['hello'],
    'hi!': ['hello_response'],
    'hiya': ['hello_response', 'hello'],
    'hiya!': ['hello_response'],
    'horse': ['horse', 'horse_slack_emoji'],
    'horse slack emoji': ['horse_slack_emoji'],
    'horse_racing': ['horse_slack_emoji'],
    'horses': ['horse'],
    'horsies': ['horse'],
    'hotdog': ['dog_slack_emoji'],
    'how are you': ['state_greeting'],
    'how are you?': ['state_greeting'],
    'how do you do': ['state_greeting'],
    'how do you do?': ['state_greeting'],
    'how have you been': ['state_greeting'],
    'how have you been?': ['state_greeting'],
    'how is it going these days': ['general_state_action'],
    'how is it going these days?': ['general_state_action'],
    'how is it hangin': ['state_greeting'],
    'how is it hanging': ['state_greeting'],
    'how is the weather': ['weather'],
    'how ya doin': ['state_greeting'],
    'how ya doing': ['state_greeting'],
    "how's it going these days": ['general_state_action'],
    "how's it going these days?": ['general_state_action'],
    "how's it hangin": ['state_greeting'],
    "how's it hanging": ['state_greeting'],
    'howdy': ['state_greeting'],
    'hows it hangin': ['state_greeting'],
    'hows it hanging': ['state_greeting'],
    'hows the weather': ['weather'],
    'howya doin': ['state_greeting'],
    'howya doing': ['state_greeting'],
    'howyadoing': ['state_greeting'],
    'how’s it been going these days?\n': ['general_state_action'],
    'hugging_face': ['positive_slack_emoji'],
    'i agree': ['agreeable_deflection'],
    "i can't agree": ['disagreeable_deflection'],
    "i can't agree more": ['agreeable_deflection'],
    'i feel your pain': ['sympathy_deflection'],
    'i hear ya ... been there myself': ['sympathy_deflection'],
    'i like them all but i really like {animal}': ['favorite_animal_response'],
    'i love mondays': ['monday_response'],
    'i love mondays!': ['monday_response'],
    'i was going to say that': ['reverse_deflection'],
    'i was going to say that.': ['reverse_deflection'],
    'i was just about to ask you that': ['reverse_deflection'],
    'i was just about to ask you that.': ['reverse_deflection'],
    "i'm glad i'm indoors": ['bad_weather_response'],
    "i'm heading outside after this chat": ['good_weather_response'],
    "i'm heading outside after this chat!": ['good_weather_response'],
    "i'm loving this weather": ['good_weather_response'],
    "i'm loving this weather.": ['good_weather_response'],
    "i'm not sure what to say": ['unknown_response'],
    "i'm ready to go outside": ['good_weather_response'],
    "i'm ready to go outside!": ['good_weather_response'],
    "i'm sorry to hear that": ['sympathy_deflection'],
    "i'm sure you're right": ['conditional_state_deflection'],
    "i've been well, thanks": ['state_greeting_response'],
    "i've been well, thanks!": ['state_greeting_response'],
    'if you say so': ['unknown_response', 'conditional_state_deflection'],
    'if you say so!': ['conditional_state_deflection'],
    'if you say so.': ['unknown_response'],
    'insult': ['insult'],
    'insult response': ['insult_response'],
    'insult slack emoji': ['insult_slack_emoji'],
    'interrogation response': ['interrogation_response'],
    'is it friday already': ['friday_response'],
    'is it friday already?': ['friday_response'],
    'it is nice to meet you': ['meet_and_greet'],
    'it is nice to meet you.': ['meet_and_greet'],
    "it's all the same to me": ['conditional_state_deflection'],
    "it's all the same to me.": ['conditional_state_deflection'],
    "it's the same old story": ['disagreeable_deflection'],
    'i’m always here': ['location_response'],
    'joy': ['positive_slack_emoji'],
    'joy_cat': ['positive_slack_emoji'],
    'just great': ['state_greeting_response'],
    'kitten': ['kitten'],
    'kittens': ['kitten'],
    'kitties': ['kitten'],
    'kitty': ['kitten'],
    'late': ['late'],
    'late transport': ['late_transport'],
    'late transport response': ['late_transport_response'],
    'leopard': ['big_cat_slack_emoji'],
    'like animal': ['like_animal'],
    'location question': ['location_question'],
    'location response': ['location_response'],
    'long time no see!\n': ['time_greeting'],
    'man that sucks': ['sympathy_deflection'],
    'man_in_lotus_position': ['neutral_slack_emoji'],
    'maybe tomorrow will be better': ['bad_weather_response'],
    'meet and greet': ['meet_and_greet'],
    'monday': ['monday'],
    'monday response': ['monday_response'],
    'mondays': ['monday'],
    'mondays, am i right': ['monday'],
    'mondays, am i right?': ['monday'],
    'my favorite animal is {animal}': ['favorite_animal_response'],
    'my favorite are {animal}': ['favorite_animal_response'],
    'nah': ['disagreeable_deflection'],
    'negative experience': ['negative_experience'],
    'negative slack emoji': ['negative_slack_emoji'],
    'neutral slack emoji': ['neutral_slack_emoji'],
    'neutral_face': ['neutral_slack_emoji'],
    'nice day': ['good_weather'],
    'nice day to go fishing': ['good_weather'],
    'nice day today': ['good_weather'],
    'nice to meet you': ['meet_and_greet'],
    'nice weather': ['good_weather'],
    "nice weather we're having": ['good_weather'],
    'no': ['disagreeable_deflection'],
    'no way': ['disagreeable_deflection'],
    'no way, jose': ['disagreeable_deflection'],
    'nope': ['disagreeable_deflection'],
    'nopers': ['disagreeable_deflection'],
    'ocelot': ['ocelot'],
    'ocelots': ['ocelot'],
    'oh geez': ['sympathy_deflection'],
    'ok': ['unknown_response'],
    'okee-dokee': ['conditional_state_deflection'],
    'otter': ['otter_slack_emoji', 'otter'],
    'otter slack emoji': ['otter_slack_emoji'],
    'otters': ['otter'],
    'packed transport': ['packed_transport'],
    'persevere': ['negative_slack_emoji'],
    'pleading_face persevere': ['negative_slack_emoji'],
    'pleased to meet you': ['meet_and_greet'],
    'positive experience': ['positive_experience'],
    'positive slack emoji': ['positive_slack_emoji'],
    'pouting_cat': ['negative_slack_emoji'],
    'pronoun': ['pronoun'],
    'puppies': ['puppy'],
    'puppy': ['puppy'],
    'racehorse': ['horse_slack_emoji'],
    'real great': ['state_greeting_response'],
    'real great man': ['state_greeting_response'],
    'real sorry to hear that': ['sympathy_deflection'],
    'response': ['response'],
    'reverse deflection': ['reverse_deflection'],
    "same o' same o'": ['cliche_deflection'],
    'same old thing': ['cliche_deflection'],
    'same same': ['cliche_deflection', 'state_greeting_response'],
    'scream': ['negative_slack_emoji'],
    'service_dog': ['dog_slack_emoji'],
    'shrug': ['neutral_slack_emoji'],
    'skull': ['negative_slack_emoji'],
    'skull_and_crossbones': ['negative_slack_emoji'],
    'slack emoji': ['slack_emoji'],
    'slightly_smiling_face': ['positive_slack_emoji'],
    'smile_cat': ['cat_slack_emoji'],
    'smiley_cat': ['cat_slack_emoji'],
    'smirk_cat': ['cat_slack_emoji'],
    'sorry to hear that': ['sympathy_deflection'],
    'state': ['state'],
    'state greeting': ['state_greeting'],
    'state greeting response': ['state_greeting_response'],
    'stuck_out_tongue': ['insult_slack_emoji'],
    'stuck_out_tongue_closed_eye': ['insult_slack_emoji'],
    'stuck_out_tongue_closed_eyes': ['positive_slack_emoji'],
    'stuck_out_tongue_winking_eye': ['insult_slack_emoji'],
    'sup': ['state_greeting'],
    'sweat': ['negative_slack_emoji'],
    'sympathy deflection': ['sympathy_deflection'],
    'tell me about what you can do': ['ability_action'],
    'tell me about yourself': ['ability_action'],
    'tell me what you can do': ['ability_action'],
    'that kinda sucks': ['sympathy_deflection'],
    'that sucks': ['sympathy_deflection'],
    "that's not suprising": ['conditional_state_deflection'],
    "that's not true": ['disagreeable_deflection'],
    'the more they stay the same': ['cliche_deflection'],
    'the more things change': ['cliche_deflection'],
    'the same old rigmarole': ['cliche_deflection'],
    "the weather doesn't impact me": ['bad_weather_response'],
    'the weather will improve': ['bad_weather_response'],
    'tiger': ['cat_slack_emoji', 'big_cat_slack_emoji'],
    'tiger2': ['big_cat_slack_emoji'],
    'time greeting': ['time_greeting'],
    'transport response': ['transport_response'],
    'unknown response': ['unknown_response'],
    'upside_down_face': ['positive_slack_emoji'],
    'wave': ['greeting_slack_emoji'],
    'weary': ['negative_slack_emoji'],
    'weather response': ['weather_response'],
    'what are you capable of': ['ability_action'],
    'what are you capable of?': ['ability_action'],
    'what are you doing': ['state_greeting', 'general_state_action'],
    'what are you doing right now?\n': ['free_state_action'],
    'what are you doing?': ['general_state_action'],
    'what are you doing?\n': ['free_state_action'],
    'what are you up to': ['general_state_action'],
    'what are you up to lately': ['general_state_action'],
    'what are you up to lately?': ['general_state_action'],
    'what are you up to right now?\n': ['free_state_action'],
    'what are you up to?': ['general_state_action'],
    'what are your capabilities': ['ability_action'],
    'what can you do': ['ability_action'],
    'what do you do': ['ability_action'],
    'what do you do for a living?\n': ['ability_action'],
    'what do you mean': ['location_response'],
    'what do you mean?': ['location_response'],
    'what is going on': ['state_greeting'],
    'what up dawg\n': ['state_greeting'],
    "what's going on": ['state_greeting'],
    "what's going on?": ['state_greeting'],
    "what's up": ['state_greeting'],
    'whatcha doing': ['general_state_action'],
    'whatcha doing?': ['general_state_action'],
    'whatcha doin’': ['general_state_action'],
    'whatcha doin’?': ['general_state_action'],
    "whats goin' on": ['state_greeting'],
    'whats going on': ['state_greeting'],
    'when will you be free': ['free_state_action'],
    'when will you be free?': ['free_state_action'],
    'where are you': ['location_question'],
    'where are you based out of': ['location_question'],
    'where are you based out of?': ['location_question'],
    'where are you?': ['location_question'],
    'where do you live': ['location_question'],
    'where do you live?': ['location_question'],
    'where you based out of': ['location_question'],
    'where you based out of?': ['location_question'],
    'wink': ['positive_slack_emoji'],
    'woman_in_lotus_position': ['neutral_slack_emoji'],
    'wow that sucks': ['sympathy_deflection'],
    'yay friday': ['friday_response'],
    'yay friday!': ['friday_response'],
    "yea ... that's no fun": ['sympathy_deflection'],
    'yes': ['good_weather_response'],
    "you can't step in the same river twice\n": ['cliche_deflection'],
    'you free': ['free_state_action'],
    'you free?': ['free_state_action'],
    'you live here': ['location_question'],
    'you live here?': ['location_question'],
    "you're adorkable": ['adorkable_response'],
    "you're pretty adorkable yourself": ['adorkable_response'],
    "you're so right": ['agreeable_deflection'],
    'zany_face': ['insult_slack_emoji'],
    '{transport} was late': ['late_transport'],
    '{transport} was packed': ['packed_transport']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
