'''Assume s is a string of lower case characters.'''

#Write a program that counts up the number of vowels contained in the string
#s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
#your program should print:

#Number of vowels: 5

def main():
    '''Vowels'''
    msit = input()
    # the input string is in s
    # remove pass and start your code here
    count = 0
    for char in msit:
        if char == 'a' or char == 'e' or char == 'i' \
        or char == 'o' or char == 'u':
            count += 1
    if count == 0:
        print("0")
    else:
        print("Vowels are : "+ str(count))

if __name__ == "__main__":
    main()
