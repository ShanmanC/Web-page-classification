#!/usr/bin/env python
# Author: Yijin Zou & Shanman Chen

import sys
import math
import re

currWord  = None
currCount = 0
currIDF = 0
word      = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        # count was not a number,
        # so silently ignore this line
        continue

    # this only works if the INPUT is sorted by key (Hadoop will do it automatically)
    if (re.match('\S+,\S+', word)):
        # if the line can match format [word,document   tf]
        # calculate the tf-idf socre and print
        # the [word,document tf-idf] key value pair
       
        #!!!!!IMPORTANT!!!! if this statement is used to caculate the IDF of the test dataset
    	currIDF = math.log(float(206) / float(currCount))
        # if want to use it the caculate the IDF for training dataset use the statement as follow
        #currIDF = math.log(float(463) / float(currCount))



        print('%s\t%s' % (word, count * currIDF))
    else:
        # if the line can match format [word    # of document]
        if currWord == word:
            currCount += count
        else:
            currCount = count
            currWord  = word

