FROM python:3
ADD solution.py /
COPY *.txt /
RUN mkdir -p /large_test
COPY large_test/* /app/src/
CMD [ "python", "./solution.py","./moby_dick.txt" ]
CMD [ "Cat","./moby_dick.txt","|","python", "./solution.py" ]
CMD [ "Cat","./large_test/*.txt","|","python", "./solution.py" ]
CMD [ "python", "./solution.py","./moby_dick.txt","./unicode_test.txt" ]
