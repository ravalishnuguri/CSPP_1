'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def word_count(string):
    '''for counting the words'''
    counts = dict()
    words = string.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
def tokenize(string):
    '''we are counting the number of words in the string'''
    newtext = ""
    newtext = "".join(string)
    newtext = newtext.strip()
    newstring1 = re.sub('[^a-zA-Z0-9]', ' ', newtext)
    # print(list(newstring1))
    # li = list(newstring1.split(" "))
    # print(li)
    # list1 = []
    # for word in newstring1:
    #   list1.append(word)
    # print(li)

    # freq1 = collections.Counter(li)
    # for word in freq1:

    print(word_count(newstring1))


def main():
    '''
        main function
    '''
    document = []
    lines = int(input())
    for i in range(lines):
        document.append(input())
        i += 1
    # print(document)
    tokenize(document)

if __name__ == '__main__':
    main()
