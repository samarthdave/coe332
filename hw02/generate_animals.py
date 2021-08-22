# https://coe-332-sp21.readthedocs.io/en/main/homework/homework01.html
import random
import json
import argparse
import petname
# python3 -m pip install petname

from utils import validate_json_file

"""
{
  "animals": [
    {
      "head": "snake",
      "body": "sheep-bunny",
      "arms": 2,
      "legs": 12,
      "tail": 14
    },
    ...

A head randomly chosen from this list: snake, bull, lion, raven, bunny
A body made up of two animals randomly chosen using the petname library
A random number of arms; must be an even number and between 2-10, inclusive
A random number of legs; must be a multiple of three and between 3-12, inclusive
A non-random number of tails that is equal to the sum of arms and legs
"""

SEED_HEADS = ["snake", "bull", "lion", "raven", "bunny"]

def build_animal():
    random_head  = random.choice(SEED_HEADS)
    random_body  = petname.Generate()
    # random, even number between 2 and 10
    # choices: - generate random between 1-5 then multiply by 2
    #                ex. 2*randint(1,5)
    #          - or
    #                ex. list(range(2, 11, 2)) --> [2, 4, 6, 8, 10]
    #                then random.choice(... list/iterable here)
    random_arms  = random.choice(range(2, 11, 2)) # start @ 2 --> 11 (exclusive end), step by 2

    # multiple of three and between 3-12, inclusive
    random_legs  = 3 * random.randint(1, 4)
    random_tails = random_arms + random_legs

    new_animal = dict(
        head=random_head,
        body=random_body,
        arms=random_arms,
        legs=random_legs,
        tail=random_tails
    )
    return new_animal

def main():
    parser = argparse.ArgumentParser(description="Generate an animal")
    parser.add_argument('output_file', type=str, nargs='?')
    args = parser.parse_args()

    # make result list
    result_lst = list()

    # add 20 new animals
    for _ in range(20):
        result_lst.append(build_animal())

    # convert to json & write to file
    write_content = {
        "animals": result_lst
    }

    OUT_FILE = args.output_file or 'animals.json'
    validate_json_file(OUT_FILE)

    # write the file with tab size 4
    with open(OUT_FILE, "w") as outfile:
        json.dump(write_content, outfile, indent=4)

if __name__ == '__main__':
    main()
