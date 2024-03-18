#!/usr/bin/python3

'''Afunction that returns a tuple with the
length of a string and its first character'''


def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        sen_length = len(sentence)
    else:
        sen_length = 0
    return (sen_length, sentence if not sentence else sentence[:1])
