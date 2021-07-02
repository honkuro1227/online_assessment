#coding=utf-8
import time
import multiprocessing
from collections import Counter
import os
import re
import sys
result_list = []

def worker(offset,length,filename):
    """
    the idea , first use regex, remain:
        1. alphanumeric
        2. -: whale-ship, is one word
        3. ': shouldn't is one word
    second, replace by ' ', then we will replace the multiple space to single space
    '         '=' '
    finally, due to we need to count continuous three words in segmentation,
    we use the left, left+1, left+2, to combine in three_word
    then we use the collections.Counter to store, the (key, frequency)
    """
    origin = open(filename, 'r')
    origin.seek(offset)
    content = origin.read(length).lower()
    content =re.sub(r"[^\w|\xe9|\362|\'|\-]",' ',content )
    content =re.sub("\s\s+" , ' ', content )   
    words = content.split(' ')
    three_words=[]
    for left in range(len(words)-3):
        three_words.append((' '.join(words[left:left+3])))
    result = Counter(three_words)
    origin.close()
    return result

def log_result(result):
    """
    global collect the result
    """
    result_list.append(result)

def stdin_case():
    """
    For read stdtest, use the single process to deal with
    """
    remain=''
    output=[]
    
    for line in sys.stdin:
        line=re.sub(r"[^\w|\xe9|\362|\'|\-]",' ',line)
        line=re.sub("\s\s+" , ' ', line)
        words=(remain+line.lower()).split(' ')           
        left=0
        for left in range(len(words)-3):
            output.append((' '.join(words[left:left+3]),1))
        remain=re.sub("\s\s+" , ' ', ' '.join(words[left+1:]))
    return output
def single_processing_stdin():
    """
    For read stdtest, use the single process to deal with
    """
    output=stdin_case()
    result=Counter(output)
    return result.most_common(100)
def multi_processing_files():
    """
    multi processing for the files, 
    1. cut the file into the chunk
    2. map to worker 
    3. return the total count table
    """
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    for filename in sys.argv[1:]:
        file_size = os.stat(filename)[6]
        token=file_size//processes
        lengths=[]
        for i in range(1,processes-1):
            lengths.append(i*token)
        lengths.append(file_size-(processes-1)*token)
        offset = 0
        for length in lengths:
            pool.apply_async(worker, args=(offset,length,filename,), callback = log_result)
            offset += length
    pool.close()
    pool.join()
    result = Counter()
    for item in result_list:
        result = result + item

    return result.most_common(100)
    

if __name__ == "__main__":
    
    """
    use the length of sys.argv to determine the 
    it is stdin case
    or 
    python solution.py file1 file2 ....
    """
    start = time.process_time()
    if len(sys.argv)==1:
        result=single_processing_stdin()
    else:
        result=multi_processing_files()    
    for word, frequency in result:
        print (word, frequency)
    print("Runtime : ",time.process_time()-start)