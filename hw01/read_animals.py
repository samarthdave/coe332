# https://coe-332-sp21.readthedocs.io/en/main/homework/homework01.html

"""
read in animals.json and print one at random
"""

import random
import json
# python3 -m pip install petname

def main():
    INPUT_FNAME = './animals.json'

    animals_lst = None
    with open(INPUT_FNAME) as input_file:
        input_dict = json.load(input_file)
        animals_lst = input_dict['animals']

    print(random.choice(animals_lst))

if __name__ == '__main__':
    main()
