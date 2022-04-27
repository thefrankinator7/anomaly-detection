import glob
import pickle
import pandas as pd
with open("length_1_dictionary.txt", "rb") as r:
   length_1_dict=pickle.load(r)
#
with open("length_2_dictionary.txt", "rb") as r:
   length_2_dict=pickle.load(r)
#
# with open("length_3_dictionary.txt", "rb") as r:
#     length_3_dict=pickle.load(r)

print("total words in dict 1:", len(length_1_dict))
print("total words in dict 2:", len(length_2_dict))
# print("total words in dict 3:", len(length_3_dict))

call_lists = []

# Recursively open files in training data to create lists of system calls
# Each file contains one trace or list of system calls
for filepath in glob.iglob("ADFA-LD\ADFA-LD\Training_Data_Clean\*.txt", recursive=True):
   with open(filepath) as current_file:
       for current_trace in current_file:
           call_lists.append(current_trace.strip())



features=pd.DataFrame(columns=['trace_length', 'length1', 'length2', 'length3', 'length4', 'length5'])



print('starting')
list_num=0
word_num=0
num_words=len(length_2_dict)
num_lists=len(call_lists)
for call_list in call_lists:
   list_num+=1
   print("currently on list", list_num,"of", num_lists)
   trace_length=len(call_list.split())
   length1_count=0
   length2_count=0
   length3_count=0
   length4_count=0
   length5_count=0
   for phrase in length_1_dict:
       if phrase in call_list:
           length1_count+=1
   for phrase2 in length_2_dict:
       word_num+=1
       index2 = call_list.find(phrase2)
       if (index2 != -1):  # length 2 words
           length2_count+=1
           for word3 in length_1_dict:
               phrase3 = ' '.join([phrase2, word3])
               index3=call_list.find(phrase3, index2, min(index2 + len(phrase3), len(call_list) - 1))
               if (index3 != -1):
                   length3_count +=1
                   for word4 in length_1_dict:
                       phrase4 = ' '.join([phrase3, word4])
                       index4 = call_list.find(phrase4, index2, min(index2 + len(phrase4), len(call_list) - 1))
                       if (index4 != -1):
                           length4_count += 1
                           for word5 in length_1_dict:
                               phrase5 = ' '.join([phrase4, word5])
                               if (call_list.find(phrase5, index2, min(index2 + len(phrase5), len(call_list) - 1)) != -1):
                                   length5_count+=1

   features = features.append(
       {'trace_length': trace_length, 'length1': length1_count, 'length2': length2_count, 'length3': length3_count,
        'length4': length4_count, 'length5': length5_count}, ignore_index=True)
   features.to_csv('clean_data.csv')

print('finished')
