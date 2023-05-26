#!/usr/bin/python3
my_return = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = my_return(sentence)
print("Length: {:d} - First character: {}".format(length, first))
