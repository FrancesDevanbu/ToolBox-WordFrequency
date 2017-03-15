""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    working_set = ''

    for line in lines:
        if not line =='\n':
            working_set = working_set + line
    working_set= working_set.split()
    wordnum = 0
    for word in working_set:
        working_set[wordnum] = word.strip(string.punctuation).lower()
        wordnum +=1

    return working_set

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    word_count = dict()
    for word in word_list:
        word_count[word] = word_count.get(word,0)+1

    ordered_by_frequency = sorted(word_count, key=word_count.get, reverse=True)

    return ordered_by_frequency[:n]

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    working_set = get_word_list('alice.txt')
    top_list = get_top_n_words(working_set, 100)

    #print("Running WordFrequency Toolbox")
    #print(string.punctuation)
    print(top_list)
