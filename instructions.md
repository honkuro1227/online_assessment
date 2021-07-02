# General Description
Welcome, Candidate. Please create a program executable from the command line that when given text(s) will return a list of the 100 most common three word sequences.

For example, if I ran `python ./solution.py moby_dick.txt` the first lines of the result would be:

```
the sperm whale - 85
the white whale - 71
of the whale - 67
```

## What to prioritize
* Basic requirements should be met.
* Basic requirements should be tested.
* Code should be well structured. Consider extensibility. Consider readability.
* Your README should include 
	* How to run your program
	* What you would do next, given more time (if anything)?
	* Any assumptions made during development
	* Are there bugs that you are aware of? 


## Basic Requirements
* The program accepts as arguments a list of one *or more* file paths (e.g. ./solution.py file1.txt file2.txt …).
* The program also accepts input on stdin (e.g. cat file1.txt | ./solution.py).
* The program outputs a list of the 100 most common three word sequences.
* The program ignores punctuation, line endings, and is case insensitive (e.g. “I love\nsandwiches.” should be treated the same as “(I LOVE SANDWICHES!!)”). Watch out that contractions aren’t changed into 2 words (eg. shouldn’t should not become shouldn t).
* The program should be tested. Provide a test file for your solution.
* The program should be well structured and understandable.
* The program is capable of processing large files and runs as fast as possible.


## Extra Credit
* The program can run in a docker container.
* The program is capable of processing large files and remains performant. Think about if the program needed to handle 1,000 Moby Dick’s at once. What would you need to do? Consider memory consumption and speed.
* It handles unicode characters(eg. the `ü` in Süsse or `ß` in Straße).


