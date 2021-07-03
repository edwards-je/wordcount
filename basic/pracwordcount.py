#!/usr/bin/python -tt

# read text file
def text_read(file):
    with open(file, 'r') as f:
        text = f.read()
    return text

# # takes in string as argument and return array of separated words, non-alphanumeric characters removed
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
    text_dict = dict_create(text)
    for key in sorted(text_dict):
        print key, text_dict[key]


# returns 20 words from most used to least
def top_count(text):
    text_dict = dict_create(text)
    sorted_list = sorted(text_dict.items(), key=lambda tup: tup[1], reverse=True)
    print(sorted_list[:20])
    

top_count('alice.txt')