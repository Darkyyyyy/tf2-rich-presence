import argparse
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join('resources', 'python', 'packages')))
sys.path.append(os.path.abspath(os.path.join('resources')))
import localization


def main():
    db_path = os.path.join('resources', 'DB.json') if os.path.isdir('resources') else 'DB.json'
    with open(db_path, 'r+') as db_json:
        db_data = json.load(db_json)

    language = db_data['settings']['language']
    loc = localization.Localizer(language=language)

    print(loc.text("TF2 Rich Presence ({tf2rpvnum}) by Kataiser"))
    print("https://github.com/Kataiser/tf2-rich-presence\n")

    parser = argparse.ArgumentParser()
    parser.add_argument('--v', default='1', help="Which version of the message to use (1 or 2)")
    message_version = parser.parse_args().v

    if message_version == '1':
        print("{}\n".format(loc.text("Launching Team Fortress 2 with Rich Presence enabled...")))
    elif message_version == '2':
        print("{}\n".format(loc.text("Launching TF2 with Rich Presence alongside Team Fortress 2...")))


if __name__ == '__main__':
    main()
