#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Code for Google's Python Class
# Copyright 2010 Google Inc.

# main() developed by Nick Parlante
# at Google Inc.

"""
A word count program as taught in Google's Python Class. Takes .txt input, cleans the text and removes 
non-alphanumeric characters, and returns an alphabetized list of word counts (--count), or the top 20
most common words (--topcount).

Usage: ./wordcount.py {--count | --topcount} <file>

Wordcount exercise
Google's Python class
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
