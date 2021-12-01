import pandas as pd
import glob

word_dictionary = {}


# Testing to create dictionary with only one trace
with open(r"ADFA-LD\ADFA-LD\Training_Data_Master\UTD-0001.txt") as training_trace:
    for line in training_trace:
        call_list = line.strip().split()


call_lists=[]

# Recursively open files in training data to create call lists
# for filepath in glob.iglob("ADFA-LD\ADFA-LD\Training_Data_Master\*.txt", recursive=True):
#     with open(filepath) as current_file:
#         for current_trace in current_file:
#             call_lists.append([current_trace.strip(), 0])





print(call_list)


# Iterate to create word dictionary
for start_index in range(len(call_list) + 1):
    for end_index in range(start_index + 50, len(call_list) + 1):
        # if end_index > start_index+5:
        #     end_index=start_index+5
        word = ' '.join(call_list[start_index:end_index])
        if word_dictionary.get(word) == None:
            word_dictionary[word] = 1
        else:
            word_dictionary[word] += 1

maxlist=max(word_dictionary, key=word_dictionary.get)

print(word_dictionary[maxlist])


