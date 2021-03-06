'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    newhand = sorted(sort(hand))
    for index in range(len(hand) - 1):
        if newhand[index+1] - newhand[index] != 1:
            return False
    return True







def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    for index in range(len(hand) - 1):
        if hand[index][1] != hand[index+1][1]:
            return False
    return True




def  is_twopair(hand):
    '''Two pair is a poker hand containing two cards of the same rank,
    two cards of another rank and one card of a third rank (the kicker)'''
    newhand = sorted(sort(hand))
    sethand = set(newhand)
    length1 = len(newhand)
    length2 = len(sethand)
    if length1 - length2 == 2:
        return True
    return False



def is_onepair(hand):
    '''One pair, or simply a pair, is a poker hand containing two cards
    of the same rank and three cards of three other ranks (the kickers)'''
    newhand = sorted(sort(hand))
    sethand = set(newhand)
    length1 = len(newhand)
    length2 = len(sethand)
    if length1 - length2 == 1:
        for index in sethand:
            if newhand.count(index) == 2:
                return index/10
    return 100


def is_threeofakind(hand):
    '''Three of a kind, also known as trips or a set, is a poker hand containing three cards
    of the same rank and two cards of two other ranks (the kickers)'''
    flag = 0
    newhand = sorted(sort(hand))
    length = len(newhand)
    for index in range(length -2):
        if newhand[index] == newhand[index+1] == newhand[index+2]:
            flag += 1
    if flag == 1:
        return True
    return False


def is_fourofakind(hand):
    '''Four of a kind, also known as quads, is a poker hand containing four cards
    of the same rank and one card of another rank (the kicker)'''
    flag = 0
    newhand = sorted(sort(hand))
    length = len(newhand)
    for index in range(length - 3):
        if newhand[index] == newhand[index+1] == newhand[index+2] == newhand[index+3]:
            flag += 1
    if flag == 1:
        return True
    return False


def is_highcard(hand):
    '''High card, also known as no pair or simply nothing, is a poker hand containing five cards
    not all of sequential rank or of the same suit'''
    #flag = 0
    newhand = sorted(sort(hand))
    length = len(newhand)
    if length == 5 and not is_flush(hand):
        return max(newhand)/100
    return False
    # for index in range(length):
    #     if newhand[index] == max(newhand):
    #         flag = 1
    # if flag == 1:
    #     return True
    # return False



def sort(hand):
    '''this function sorts  and change the letter values to numbers for example,
    it will change 'J' value as 11'''
    newhand = []
    length = len(hand)
    for index in range(length):
        if hand[index][0] == 'A':
            newhand.append(14)
        elif hand[index][0] == 'K':
            newhand.append(13)
        elif hand[index][0] == 'Q':
            newhand.append(12)
        elif hand[index][0] == 'J':
            newhand.append(11)
        elif hand[index][0] == 'T':
            newhand.append(10)
        else:
            newhand.append(int(hand[index][0]))
    return newhand

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if is_straight(hand) and is_flush(hand):
        return 8
    if is_threeofakind(hand) and is_onepair(hand):
        return 7
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    if is_fourofakind(hand):
        return 4
    if is_threeofakind(hand):
        return 3
    if is_twopair(hand):
        return 2
    if is_onepair(hand) != 100:
        return is_onepair(hand)
    return is_highcard(hand)

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
