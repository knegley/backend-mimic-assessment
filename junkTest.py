#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Kyle Negley - Daniel helped me refacotr my craziness of a while loop to use a for loop amd simplify my code"

import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """

    with open(filename, "r") as f:
        # print(type((f.read().split())))
        mimic_list = [word for word in f.read().split()]

    # print(mimic_list)

    mimic_dict = {}
    mimic_dict[""] = mimic_list[0]

    for index, word in enumerate(mimic_list):
        if index+1 == len(mimic_list):
            break

        # print(index)

        if word not in mimic_dict:
            mimic_dict[word] = [mimic_list[index+1]]

        elif word in mimic_dict:
            mimic_dict[word].append(mimic_list[index+1])

    # print(f"mimic_dict: {mimic_dict}")
    return mimic_dict


create_mimic_dict("imdev.txt")


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """

    #print(mimic_dict.get(start_word, f"{start_word} not found in dictionary"))

    # print("")
    # if start_word not in mimic_dict:
    #     return

    # result = [random.choice(mimic_dict[start_word])]

    start_words = list(mimic_dict.keys())
    start_word = start_word

    # start word is random and use as key
    for _ in range(200):
        print(start_word)

        start_word = random.choice(mimic_dict[random.choice(start_words)])
        # result = [
        #     *result, random.choice(mimic_dict[random.choice(start_words)])]
        # print(random.choice(mimic_dict[random.choice(start_words)]))

    # print(" ".join(result))


# print_mimic(create_mimic_dict("imdev.txt"), "I")
# print_mimic(create_mimic_dict("imdev.txt"), "pizza")


# Provided main(), calls mimic_dict() and print_mimic()


def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
