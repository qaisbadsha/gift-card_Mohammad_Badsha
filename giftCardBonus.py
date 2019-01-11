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

    # we will apply same logic as for two gifts, except keep "shrinking" the list
    # with the third element starting from lowest to highest.
    low = 1
    high = len(gifts) - 1
    third = 0

    # default in case we find nothing
    gift1 = ['No gift possible', -1]
    gift2 = ['No gift possible', -1]
    gift3 = ['No gift possible', -1]

    # till we are at the final three
    while third < len(gifts) - 2:

        # adding once initially before loop
        sum = gifts[low][1] + gifts[high][1] + gifts[third][1]

        while low < high:
            if target - sum < diff and target - sum >= 0:

                # Every time we get a closer value, store it
                gift1 = gifts[high]
                gift2 = gifts[low]
                gift3 = gifts[third]
                diff = min(diff, target - sum)

            if sum > target:

                # go cheaper
                high -= 1
            else:

                # spend more
                low += 1

            sum = gifts[low][1] + gifts[high][1] + gifts[third][1]

        # so by incrementing third, we shrink the list and go over the cycle again
        third += 1
        low = third + 1
        high = len(gifts) - 1

    print gift1
    print gift2
    print gift3


gift_finder()
