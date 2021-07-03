#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# read text file
def text_read(file):
    with open(file, 'r') as f:
        text = f.read()
    return text

# takes in string as argument and return array of separated words, non-alphanumeric characters removed
def clean_text(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz \''
    cleantext = ""
    text = text_read(text).lower()
    for i in text:
        if i in alphabet:
            cleantext += i
        else:
            cleantext += ' '
    cleantext = cleantext.split()
    cleantext[:] = [x for x in cleantext if x != '\'']
    
    return(cleantext)

# count and add words to dictionary
def count_append(words, word_count_hash):
    for i in words:
        if word_count_hash.has_key(i):
            word_count_hash[i] += 1
        else:
            word_count_hash[i] = 1

    #print(word_count_hash)
    return(word_count_hash)


# create dicitonary from text
def dict_create(seed):
    words_array = clean_text(seed)
    count_dict = {}
    count_dict = count_append(words_array, count_dict)
    return(count_dict)


# returns sorted count in <word 1, count 1> format: for --count
def print_words(text):
    text_dict = dict_create(text  )
    for key in sorted(text_dict):
        s = "."
        print (str(key) + " " +  s*(12 - len(key)) + str(text_dict[key]))


# returns 20 words from most used to least
def print_top(text):
    text_dict = dict_create(text)
    sorted_list = sorted(text_dict.items(), key=lambda tup: tup[1], reverse=True)
    for key in sorted_list[:20]:
      s = "."
      print(str(key[0]) + " " + s*(12 - len(key[0])) + str(key[1]))

def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  print("Argument List:", str(sys.argv))
  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
    # print("Hello from --count")
  elif option == '--topcount':
    # print("Hello from --topcount")
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
