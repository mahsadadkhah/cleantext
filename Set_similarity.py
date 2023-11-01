from hazm import *
import os
from docx import Document
import pandas as pd
import re
import numpy as np
from Clean_main import *


text1 = """
علی و محسن به همراه نادر به مدرسه در روزهای پاییزی میروند.
زهرا به مدرسه همراه خواهرش رفت ولی محمد به مدرسه نرفت.
غذا سرد است.
"""
text2 = """
علی و حسن به همراه نادری در روزهای پاییزی به مدرسه رفتند
زهرا به دانشگاه می رود.
 چه روز زیبایی است.
"""



alpha = fix_half_space(text1)
beta = remove_consecutive_duplicates(alpha)
gamma = verb_tokenizer(beta)
epsilon = modify_sentences(gamma)
clean_text1 = word_tokener(epsilon)

print("cleaned text1:", clean_text1)


a = fix_half_space(text2)
b = remove_consecutive_duplicates(a)
c = verb_tokenizer(b)
d = modify_sentences(c)
clean_text2 = word_tokener(d)
print("cleaned text2:", clean_text2)

texts = text1 + text2
all_text = fix_half_space(texts)
all_1 = remove_consecutive_duplicates(all_text)
all_2 = verb_tokenizer(all_1)
all_3 = modify_sentences(all_2)
clean_texts = word_tokener(all_3)
print("all text cleaned:", clean_texts)


def list_to_set(list_sent):
  word_set = set()
  for sentence in clean_texts:
    for word in sentence:
      word_set.add(word)
  return word_set


def find_index(text, set_dict):
  indices = []
  for token in text:
    if token in set_dict:
      indices.append(set_dict[token])
  return indices

def IntersectionTwoLists(list1, list2):
    return set(list1).intersection(list2)


vocabs = sorted(list_to_set(clean_texts))
word2idx = {u:i for i, u in enumerate(vocabs)}
idx2word = np.array(vocabs)
print(word2idx)


text1_list = []
for sentent in clean_text1:
    text_as_int = np.array([word2idx[word] for word in sentent])
    text1_list.append(text_as_int)


text2_list = []
for sentent in clean_text2:
    text_as_int = np.array([word2idx[word] for word in sentent])
    text2_list.append(text_as_int)

print(text2_list)
print(text1_list)

text1_size = len(text1_list)
text2_size = len(text2_list)
print(text1_size)
print(text2_size)


sim_arr = np.zeros((text1_size, text2_size))


for i, sentent1 in enumerate(text1_list):
    for j, sentent2 in enumerate(text2_list):
        itersect = IntersectionTwoLists(sentent1, sentent2)
        if(len(itersect) != 0):
            sim_arr[i][j] = round(len(itersect)/len((sentent1)), 2)
print(sim_arr)

most_sim = np.argmax(sim_arr, axis=0)

print('متن اول:' + text1)
print('متن دوم:' + text2)
print("جملات مشابه: ")
for i, x in enumerate(most_sim):
    if sim_arr[x][i] > .4 :
        print(text1.split('.')[x].replace('\n','') + ' ' + str(sim_arr[x][i]))


