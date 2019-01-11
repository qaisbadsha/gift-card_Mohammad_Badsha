#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def gift_finder():

    # get a list of rows
    lines = [line.rstrip('\n') for line in open(sys.argv[1])]

    gifts = list()

    # put each row, as a list, in our list of gifts
    for line in lines:
        gift = line.split(',')
        gift[1] = int(gift[1])
        gifts.append(gift)

    target = int(sys.argv[2])

    # get the biggest number possible for initial differnce
    diff = float('inf')

    if gifts is None or len(gifts) == 0:
        print 'Provide a normal gift card please'

    # we will start a pointer from the bottom and top of the list,
    # if the total is 'cheaper' we can spend more and move lower pointer
    # while if it costs too much we will spend less and move the higher pointer

    low = 0
    high = len(gifts) - 1

    # default in case we find nothing
    gift1 = ['No gift possible', -1]
    gift2 = ['No gift possible', -1]

    # adding once initially before loop
    sum = gifts[low][1] + gifts[high][1]

    while low < high:
        if target - sum < diff and target - sum >= 0:

            # Ever time we get a closer value, store it
            gift1 = gifts[high]
            gift2 = gifts[low]
            diff = min(diff, target - sum)

        if sum > target:

            # go cheaper
            high -= 1
        else:

            # spend more
            low += 1

        sum = gifts[low][1] + gifts[high][1]

    print gift1
    print gift2


gift_finder()
