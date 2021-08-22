# https://coe-332-sp21.readthedocs.io/en/main/homework/homework01.html

"""
read in animals.json and print one at random
"""

import random
import json
import argparse
# python3 -m pip install petname

from utils import validate_json_file

def main():
    parser = argparse.ArgumentParser(description="Generate an animal")
    parser.add_argument('output_file', type=str, nargs='?')
    args = parser.parse_args()

    INPUT_FNAME = args.output_file or 'animals.json'
    validate_json_file(INPUT_FNAME)

    animals_lst = None
    with open(INPUT_FNAME) as input_file:
        input_dict = json.load(input_file)
        animals_lst = input_dict['animals']

    print(random.choice(animals_lst))

if __name__ == '__main__':
    main()
