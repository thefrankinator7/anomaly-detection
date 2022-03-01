import operator

import pandas as pd
import glob
import pickle
from itertools import dropwhile
from itertools import islice

# # Testing to create dictionary with only one trace
# with open(r"ADFA-LD\ADFA-LD\Training_Data_Master\UTD-0001.txt") as training_trace:
#     for line in training_trace:
#         call_list = line.strip().split()

call_lists = []

# Recursively open files in training data to create lists of system calls
# Each file contains one trace or list of system calls
for filepath in glob.iglob("ADFA-LD\ADFA-LD\Training_Data_Clean\*.txt", recursive=True):
    with open(filepath) as current_file:
        for current_trace in current_file:
            call_lists.append(current_trace.strip().split())

# call_lists=call_lists[0:399]
print("Number of traces in training data: ", len(call_lists))

word_dictionary = {}

# Iterate to create word dictionary
list_index = 0
total_possible_words = 0
# print(call_lists)
for call_list in call_lists:
    list_index += 1
    # print("Working on Trace:", list_index)
    for start_index in range(len(call_list) + 1):
        for end_index in range(start_index + 1, min(len(call_list) + 1, start_index + 6)):
            total_possible_words += 1
            word = ' '.join(call_list[start_index:end_index])
            # print(word)
            if word_dictionary.get(word) == None:
                word_dictionary[word] = 1
            else:
                word_dictionary[word] += 1

# Remove words below a count of 250
for key, count in dropwhile(lambda key_count: key_count[1] >= 250,
                            sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)):
    del word_dictionary[key]

print("Total possible words:", total_possible_words)

maxlist = max(word_dictionary, key=word_dictionary.get)

print("Most occurrences of a word:", word_dictionary[maxlist])

total_words = len(word_dictionary)
print("total words", total_words)

# Create phrase dictionaries of lengths 1-4

phrase_dictionary1 = {}
phrase_dictionary2 = {}
phrase_dictionary3 = {}
phrase_dictionary4 = {}
word2_index = 0

#Iterate to create every possible phrase from the words (this takes too long)
for word1 in word_dictionary:
    phrase_dictionary1[word1] = 1

with open("length_1_dictionary.txt", "wb") as w:
    pickle.dump(phrase_dictionary1, w)

# length 2
for word1 in word_dictionary:
    for word2 in word_dictionary:
        phrase = ' '.join([word1, word2])
        phrase_dictionary2[phrase] = 1

with open("length_2_dictionary.txt", "wb") as w:
    pickle.dump(phrase_dictionary2, w)

#length 3
word1_index = 0
for word1 in word_dictionary:
    print("Currently at word", word1_index, "of", total_words)
    word1_index += 1
    for word2 in word_dictionary:
        for word3 in word_dictionary:
            phrase = ' '.join([word1, word2, word3])
            phrase_dictionary3[phrase] = 1

with open("length_3_dictionary.txt", "wb") as w:
    pickle.dump(phrase_dictionary3, w)

# with open("length_3_dictionary.txt", "rb") as r:
#     phrase_dictionary3 = pickle.load(r)


# def chunks(data, SIZE=10):
#     it = iter(data)
#     for i in range(0, len(data), SIZE):
#         yield {k:data[k] for k in islice(it, SIZE)}

# print("starting last dictionary")
# word_index=0
# for word in word_dictionary:
#     word_index+=1
#     if word_index>315:
#         phrase_dictionary4_current={}
#         print("Currently on word %s of 317" %word_index)
#         for phrase1 in phrase_dictionary3:
#             phrase = ' '.join([word, phrase1])
#             phrase_dictionary4_current[phrase] = 1
#
#         with open("D:\Phrase Dictionaries\length_4_dictionary%s.txt" %word_index, "wb") as w:
#             pickle.dump(phrase_dictionary4_current, w)






# print("starting last dictionary")
# chunk_index = 0
# word_index=0
# for dict_chunk in chunks(word_dictionary, 317):
#     chunk_index+=1
#     print("Currently on chunk %s of 317" %chunk_index )
#     phrase_dictionary4_current={}
#     for word in dict_chunk:
#         word_index+=1
#         print("Currently on word %s of 317" %word_index)
#         for phrase1 in phrase_dictionary3:
#             phrase = ' '.join([word, phrase1])
#             phrase_dictionary4_current[phrase] = 1
#
#     with open("D:\Phrase Dictionaries\length_4_dictionary%s.txt" %chunk_index, "wb") as w:
#         pickle.dump(phrase_dictionary4_current, w)
