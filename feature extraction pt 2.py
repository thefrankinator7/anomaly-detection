import glob
import pickle
import pandas as pd
with open("length_1_dictionary.txt", "rb") as r:
    length_1_dict=pickle.load(r)
#
with open("length_2_dictionary.txt", "rb") as r:
    length_2_dict=pickle.load(r)
#
with open("length_3_dictionary.txt", "rb") as r:
    length_3_dict=pickle.load(r)
#
# print("total words in dict 1:", len(length_1_dict))
# print("total words in dict 2:", len(length_2_dict))
# print("total words in dict 3:", len(length_3_dict))

call_lists = []

# Recursively open files in training data to create lists of system calls
# Each file contains one trace or list of system calls
for filepath in glob.iglob("ADFA-LD\ADFA-LD\Training_Data_Clean\UTD-00*.txt", recursive=True):
    with open(filepath) as current_file:
        for current_trace in current_file:
            call_lists.append(current_trace.strip())


features=pd.DataFrame(columns=['trace_length', 'length1', 'length2', 'length3', 'length4'])



print('starting')
list_num=0
num_lists=len(call_lists)
for call_list in call_lists:
    list_num+=1
    print("currently on list", list_num,"of", num_lists)
    trace_length=len(call_list.split())
    length1_count=0
    length2_count=0
    length3_count=0
    length4_count=0
    for phrase in length_1_dict:
        if phrase in call_list:
            length1_count+=1
    for phrase2 in length_2_dict:
        index = call_list.find(phrase2)
        if (index != -1):
            length2_count+=1
            for word in length_2_dict:
                phrase4 = ' '.join([phrase2, word])
                if (call_list.find(phrase4, index, min(index + len(word) + 10, len(call_list) - 1)) != -1):
                    length4_count += 1
    for phrase in length_3_dict:
        if phrase in call_list:
            length3_count+=1
    features=features.append({'trace_length': trace_length, 'length1' : length1_count, 'length2': length2_count, 'length3': length3_count, 'length4': length4_count}, ignore_index=True)
    if (list_num % 10 == 0):
        features.to_csv('temp_attack_data%s.csv' %list_num)

# length4_count=[]
# list_num=0
# phrase2len=len(length_2_dict)
# for call_list in call_lists:
#     list_num+=1
#     print("currently on list", list_num,"of", num_lists)
#     phrase_count=0
#     phrase_num=0
#     for phrase2 in length_2_dict:
#         phrase_num+=1
#         #print("Currently on phrase %d of" %phrase_num, phrase2len)
#         index=call_list.find(phrase2)
#         if (index != -1):
#             for word in length_2_dict:
#                 phrase4=' '.join([phrase2, word])
#                 if (call_list.find(phrase4, index, min(index+len(word)+10, len(call_list)-1)) !=-1):
#                     phrase_count+=1
#     length4_count.append(phrase_count)
#     if (list_num%50==0):
#         temp_list=length4_count
#         temp_dict={'length 4': temp_list}
#         temp_data=pd.DataFrame(temp_dict)
#         temp_data.to_csv('temp_length4_%s.csv' %list_num)








print('finished')
# features=features.append({'length1' : 10, 'length2': 4, 'length3': 14}, ignore_index=True)

# features=pd.read_csv("feature dataset clean only.txt")
# features['length 4'] = length4_count


print(features)

features.to_csv("feature dataset attack master.txt")
