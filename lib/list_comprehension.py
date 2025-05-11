#!/usr/bin/env python3

def return_evens(num_list):
    # Use a list comprehension to filter even numbers
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    # Use a list comprehension to add an exclamation mark to each sentence
    return [sentence + "!" for sentence in sentence_list]