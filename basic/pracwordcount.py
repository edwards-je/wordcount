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
def clean_text(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    cleantext = ""
    text = text.lower()
    for i in text:
        if i in alphabet:
            cleantext += i
        else:
            cleantext += ' '

    return cleantext

splitted = clean_text(seed)
splitted = splitted.split() #split text 
print(splitted)

# dict2 = {}    


# # count and add words to dictionary
# for i in splitted:
#     if dict2.has_key(i):
#         dict2[i] += 1
#     else:
#         dict2[i] = 1

# print(dict2)