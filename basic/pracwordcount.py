import re

#seed text
seed = '''Presently she began again.  `I wonder if I shall fall right
THROUGH the earth!  How funny it'll seem to come out among the
people that walk with their heads downward!  The Antipathies, I
think--' (she was rather glad there WAS no one listening, this
time, as it didn't sound at all the right word) `--but I shall
have to ask them what the name of the country is, you know.
Please, Ma'am, is this New Zealand or Australia?' (and she tried
to curtsey as she spoke--fancy CURTSEYING as you're falling
through the air!  Do you think you could manage it?)  `And what
an ignorant little girl she'll think me for asking!  No, it'll
never do to ask:  perhaps I shall see it written up somewhere.
'''

# takes in string as argument and return array of separated words, non-alphanumeric characters removed
def clean_text(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    cleantext = ""
    text = text.lower()
    for i in text:
        if i in alphabet:
            cleantext += i
        else:
            cleantext += ' '

    return cleantext.split()



# count and add words to dictionary
def count_append(words, word_count_hash):
    for i in words:
        if word_count_hash.has_key(i):
            word_count_hash[i] += 1
        else:
            word_count_hash[i] = 1

    #print(word_count_hash)
    return(word_count_hash)

words_array = clean_text(seed)
count_dict = {}

count_dict = count_append(words_array, count_dict)
print(count_dict)
#test comment