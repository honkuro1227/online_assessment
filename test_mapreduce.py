import collections
import itertools
import multiprocessing
import re
import time
import operator
import sys
class MapReduce(object):
    
    def __init__(self, map_function, reduce_function, num_workers=None):
        """
        map_func: map function
        reduce_func: reduce function
        pool : multiprocessing pool
        """
        self.map_function = map_function
        self.reduce_function = reduce_function
        self.pool = multiprocessing.Pool(num_workers)
    
    def partition(self, mapped_values):
        """
        map values
        """
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()
    
    def __call__(self, inputs):
        """
        main function map-> then go to reducer
        """
        map_responses = self.pool.map(self.map_function, inputs)
        partitioned_data = self.partition(itertools.chain(*map_responses))
        reduced_values = self.pool.map(self.reduce_function, partitioned_data)
        return reduced_values




def file_to_words(filename):
    """
    Read a file and return a sequence of (word, occurances) values.
    """
    output = []
    with open(filename, 'r') as f:
        remain=''
        for line in f:
            line=re.sub(r"[^\w|\xe9|\362|\'|\-]",' ',line)
            line=re.sub("\s\s+" , ' ', line)
            words=(remain+line.lower()).split(' ')           
            left=0
            for left in range(len(words)-3):
                output.append((' '.join(words[left:left+3]),1))
            remain=re.sub("\s\s+" , ' ', ' '.join(words[left+1:]))
        return output


def count_words(item):
    """
    reducer, convert mapvalues into tuple of the word,occurences
    """
    word, occurances = item
    return (word, sum(occurances))


if __name__ == '__main__':
    start=time.process_time()

    process=4
    input_files=sys.argv[1:]
    word_counts =None
    for file in input_files:
        mapper = MapReduce(file_to_words, count_words,process)
        word_counts = mapper([file])
        word_counts.sort(key=operator.itemgetter(1))
        word_counts.reverse()
    print ('\n top 100 words by frequency \n')
    top100 = word_counts[:100]
    print(top100)
    print("Runtime : ",time.process_time()-start)
