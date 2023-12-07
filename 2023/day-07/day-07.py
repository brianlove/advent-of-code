#! /usr/bin/env python3

import argparse
import collections
import functools

parser = argparse.ArgumentParser("Day 7")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

# CARD_ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
CARD_ORDER = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARD_ORDER_PT2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


FIVE_KIND  = 6
FOUR_KIND  = 5
FULL_HOUSE = 4
THREE_KIND = 3
TWO_PAIR   = 2
ONE_PAIR   = 1
HIGH_CARD  = 0

TYPES = [
    'high-card',
    '1-pair',
    '2-pair',
    '3-kind',
    'full-house',
    '4-kind',
    '5-kind',
]

def categorize_hand(hand):
    # print()
    hand_dd = collections.defaultdict(lambda: 0)
    for c in hand:
        hand_dd[c] += 1

    # print(hand, " --> ", hand_dd.items())
    grouping = list(hand_dd.items())
    grouping.sort(key=lambda x: x[1], reverse=True)

    strength = [CARD_ORDER.index(c) for c in hand]

    # print(grouping)

    if grouping[0][1] == 5:
        return [FIVE_KIND, strength, grouping]

    elif grouping[0][1] == 4:
        return [FOUR_KIND, strength, grouping]

    elif grouping[0][1] == 3 and grouping[1][1] == 2:
        return [FULL_HOUSE, strength, grouping]

    elif grouping[0][1] == 3:
        return [THREE_KIND, strength, grouping]

    elif grouping[0][1] == 2 and grouping[1][1] == 2:
        return [TWO_PAIR, strength, grouping]

    elif grouping[0][1] == 2:
        return [ONE_PAIR, strength, grouping]

    else:
        return [HIGH_CARD, strength, grouping]



INDEX_HAND = 0
INDEX_TYPE = 1
INDEX_STRENGTH = 2
INDEX_GROUP = 3
INDEX_BID = 4



def part1(lines):
    print("\n\n~~ PART 1~~")

    hand_list = []

    for line in lines:
        # print()
        hand, bid = line.split(' ')
        # print("Hand: ", hand)
        hand_type, strength, grouping = categorize_hand(hand)
        # print("  ", TYPES[hand_type], hand_type, grouping)

        hand_list.append(
            (hand, hand_type, strength, grouping, int(bid))
        )

    hand_list.sort(key=lambda x: (x[INDEX_TYPE], x[INDEX_STRENGTH]), reverse=True)

    num_hands = len(hand_list)
    winnings = []

    print()
    for (ix, hand) in enumerate(hand_list):
        rank = num_hands - ix
        # print(hand[INDEX_HAND], rank, '*', hand[INDEX_BID], "=", rank * hand[INDEX_BID])
        winnings.append(rank * hand[INDEX_BID])

    # print(winnings)
    print("Total", functools.reduce(lambda x,y: x + y, winnings, 0))



def categorize_hand_pt2(hand):
    # print()
    hand_dd = collections.defaultdict(lambda: 0)

    num_jokers = hand.count("J")
    hand_no_jokers = hand.replace("J", "")

    for c in hand_no_jokers:
        hand_dd[c] += 1

    # print(hand, " --> ", hand_dd.items())
    grouping = list(hand_dd.items())
    grouping.sort(key=lambda x: x[1], reverse=True)
    counts = list(map(lambda x: x[1], grouping))

    strength = [CARD_ORDER_PT2.index(c) for c in hand]

    # print(f"Hand: {hand}, num_jokers: {num_jokers}, strength:", strength, "grp_cts", grouping_counts)

    if num_jokers == 5 or counts[0] + num_jokers == 5:
        hand_type = FIVE_KIND
    elif counts[0] + num_jokers == 4:
        hand_type = FOUR_KIND

    ## At this point we know that we have AT MOST 2 jokers, since if there were
    ## 3 jokers, those plus any other card would equal FOUR_KIND

    ## Types of 2 joker hands
    ## - JJAAA --> 5 of kind
    ## - JJAAB --> 4 of kind
    ## - JJABB --> 4 of kind
    ## - JJABC --> 3 of kind

    ## So we can't have a full house with 2 jokers!

    ## - JAAAB --> full house (J = B)
    ## - JAABB --> full house (J = A)



    elif (
        (counts[0] == 3 and counts[1] == 2) or
        (counts[0] == 3 and counts[1] == 1 and num_jokers == 1) or
        (counts[0] == 2 and counts[1] == 2 and num_jokers == 1)
    ):
        hand_type = FULL_HOUSE

    ## - JAABC --> 3 of kind
    ## - JJABC --> 3 of kind (alredy handled)
    elif (
        (counts[0] == 3) or
        (counts[0] == 2 and num_jokers == 1) or
        (counts[0] == 1 and num_jokers == 2)
    ):
        hand_type = THREE_KIND

    ## - JABCD --> 1 pair

    elif counts[0] == 2 and counts[1] == 2:
        hand_type = TWO_PAIR

    elif (
        (counts[0] == 1 and counts[1] == 1 and num_jokers == 1) or
        (counts[0] == 2 and num_jokers == 0)
    ):
        hand_type = ONE_PAIR

    else:
        hand_type = HIGH_CARD

    return [hand_type, strength, grouping]


def part2(lines):
    print("\n\n~~ PART 2~~")

    hand_list = []

    for line in lines:
        print()
        hand, bid = line.split(' ')
        print("Hand: ", hand)
        hand_type, strength, grouping = categorize_hand_pt2(hand)
        print("  ", TYPES[hand_type], hand_type, grouping)

        hand_list.append(
            (hand, hand_type, strength, grouping, int(bid))
        )

    hand_list.sort(key=lambda x: (x[INDEX_TYPE], x[INDEX_STRENGTH]), reverse=True)

    num_hands = len(hand_list)
    winnings = []

    print()
    for (ix, hand) in enumerate(hand_list):
        rank = num_hands - ix
        # print(hand[INDEX_HAND], rank, '*', hand[INDEX_BID], "=", rank * hand[INDEX_BID])
        winnings.append(rank * hand[INDEX_BID])

    # print(winnings)
    print("Total", functools.reduce(lambda x,y: x + y, winnings, 0))


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    part1(lines)

    part2(lines)
