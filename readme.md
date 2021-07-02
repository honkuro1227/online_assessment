## Basic Requirements
- [x] The program accepts as arguments a list of one *or more* file paths (e.g. ./solution.py file1.txt file2.txt …).
- [x] The program also accepts input on stdin (e.g. cat file1.txt | ./solution.py).
- [x] The program outputs a list of the 100 most common three word sequences.
- [x] The program ignores punctuation, line endings, and is case insensitive (e.g. “I love\nsandwiches.” should be treated the same as “(I LOVE SANDWICHES!!)”). Watch out that contractions aren’t changed into 2 words (eg. shouldn’t should not become shouldn t).(O)
- [x] The program should be tested. Provide a test file for your solution. (remain test file)
- [x] The program should be well structured and understandable.
- [x] The program is capable of processing large files and runs as fast as possible.
## Extra Credit
- [x] The program can run in a docker container.
- [x] The program is capable of processing large files and remains performant. Think about if the program needed to handle 1,000 Moby Dick’s at once. What would you need to do? Consider memory consumption and speed.
- [x] It handles unicode characters(eg. the `ü` in Süsse or `ß` in Straße). ()
## How to run the file
### default test file
I put the following test file in same folder
  Alices-Adventures-in-Wonderland-by-Lewis-Carroll.txt: novel 54KB
  Anne-of-Green-Gables.txt: 548
  moby_dick.txt: 1228kb 
  unicode_test.txt: 1090 , contain unicode characters
  unicode_mix_normal_word.txt: 1kb, hybrid normal and unicode
I copy around 50 moby_dick.txt in the large_test and I put the file in the large_test on the docker too\n
### Launch docker:
In the terminal:
  $docker pull honkuro/new_relic:v2\
  $docker run -t -i --rm honkuro/new_relic:v2 bash\
Then, you can use following code to run my code
### in the bash terminal
1. python ./solution.py file1.txt file2.txt ...etc\
for instance, 
  python ./solution.py ./moby_dick.txt\
In this case, solution.py will treat the filename as input do the word count. I have two testcase one is moby_dick.txt, and other is unicode_test which contaion the unicode case
2. cat file | python ./solution.py\
In this case, solution.py will readline from stdin\
there are two cases:\
  single: cat ./moby_dick.txt | python ./solution.py\
  Large_test: cat ./app/src/*.txt| python ./solution.py\

## What you would do next, given more time (if anything)?
If I am given more time, I will try to:
1. try more test cases: since I time and computing resource limit, I cannot test the very large file
to make sure the multiprocessing performance is better than single processing.
2. I would like to test more different multiprocessing or the MapReduce function. In this assignment
I try the single, multiprocessing, and MapReduce. I found the MapReduce solution does not perform well.
I think the reason is the overhead of the map transfer to the reducer is much larger than the use of the counter
directly.
3. Try the existing library solution for the word count.
Since this is the taking-home assignment, I try to implement all the detail of the code without the library.
If I have the time, I will try some MapReduce or the parallel programming library, such as Hadoop MapReduce
or Spark.

## Any assumptions made during development
First, although I try to make the single output the same as the instruction. However, I find contradictions
between basic requirements. For the "of the whale - 67", I found my number is not the same as the output. I try
to figure out what causes the issue. Via my human eye debugs, I found the 67 will only occur while I treat
"of the\nwhale"!= "of the whale", which contradicts the basic requirements:
"""
The program ignores punctuation, line endings,
and is case insensitive (e.g. “I love\nsandwiches.”
should be treated the same as “(I LOVE SANDWICHES!!)”).
Watch out that contractions aren’t changed into 2 words
(eg. shouldn’t become shouldn't)."
"""
## Are there bugs that you are aware of?
Currently, I think there are no bugs in my code.
I think the only possibility is the version different in the commend
line.
