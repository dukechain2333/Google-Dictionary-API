import json
from requests import Session
import os
from playsound import playsound


def url(lang: str, word: str) -> str:
    return f"https://api.dictionaryapi.dev/api/v2/entries/{lang}/{word}"


try:
    with open('welcome', 'r') as f:
        welcome = f.read()
    with open('config.json', 'r') as f:
        config = json.load(f)
    with open('language_list', 'r') as f_:
        language_list = f_.read()
except (FileNotFoundError, json.JSONDecodeError):
    input('Program files incomplete. Press enter to exit.')
    exit(0)
os.system('')
print(welcome)
sess = Session()
sess.trust_env = False


def set_language(*args):
    config['language'] = args[0]


def display_language_table(*args):
    print(language_list)


def display_history(*args):
    print(', '.join(config['history']))


def clear_history(*args):
    config['history'] = []


def save():
    with open('config.json', 'w') as f_:
        json.dump(config, f_)


def set_tracking_preference(*args):
    config['track'] = args[0]


def play_pronunciation(*args):
    playsound('https:' + args[0])


hashed_function = {
    "ls": set_language, "ll": display_language_table,
    "hp": display_history, "hc": clear_history, "ht": set_tracking_preference,
    "p": play_pronunciation,
    "s": save,
}


while True:
    query = input("> ")
    if query[0] == '@':
        cmd = query[1:].split()
        hashed_function[cmd[0]](*cmd[1:])
    else:
        response = sess.get(url(config['language'], query), verify=True)
        if response.status_code != 200:
            print('Network error: status =', response.status_code)
            print('* The 404 error will occur if the word does not exist.')
        else:
            if config['track'] == 'on':
                config['history'] = [query] + config['history']
            meaning = json.loads(response.text)[0]
            display = ['\33[35m' + meaning['word'] + '\33[0m', '\33[31mPhonetics:\33[0m']
            for phonetic in meaning['phonetics']:
                display.append('    ' + phonetic['text'] + '    ' +
                               phonetic['audio'] if 'audio' in phonetic.keys() else '')
            display.append('\33[31mMeaning:\33[0m')
            for meaning_ in meaning['meanings']:
                if 'partOfSpeech' in meaning_.keys():
                    display.append('    \33[33m' + meaning_['partOfSpeech'] + '\33[0m')
                for def_ in meaning_['definitions']:
                    display.append(def_['definition'])
                    if 'example' in def_.keys() and def_['example']:
                        display.append('    \33[32me.g. ' + def_['example'] + '\33[0m')
                    if 'synonyms' in def_.keys() and def_['synonyms']:
                        display.append('    \33[34msynonyms: ' + ', '.join(def_['synonyms']) + '\33[0m')
            print(*display, sep='\n')
