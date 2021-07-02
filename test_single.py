# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:01:26 2021

@author: fghjk
"""

"""
idea
basic case
use hash_table to remember the three word:key, number of time comes out
ignore the punctuation, insensitive 
"""
import re

from collections import Counter
import time
import sys
input_files = sys.argv[1:]
three_word=[]
for filename in input_files:
    print('hi')
    origin=open(filename,'r').read().lower()
    origin=re.sub(r"[^\w|\xe9|\362|\'|\-]",' ',origin)
    origin=re.sub("\s\s+" , " ", origin)
    words=origin.split(' ')
    left=0
    for left in range(len(words)-3):
        three_word.append(' '.join(words[left:left+3]))
start=time.process_time()
result = Counter(three_word).most_common(100)
for word, frequency in result:
    print(word,frequency)
print("Runtime : ",time.process_time()-start)
