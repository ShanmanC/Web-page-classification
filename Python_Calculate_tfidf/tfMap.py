#!/usr/bin/env python
# Author: Yijin Zou & Shanman Chen

import sys
import re
import os

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    filename = os.environ['mapreduce_map_input_file']
    # shorten the filename, only remain the book name.
    filename = re.sub('\S+projectdata/', '', filename)
    # split the line into words
    words = filter(None, re.split('\W+|[_]+', line))
    # write out word paired with count of 1
    for word in words:
        # write the results to STDOUT (standard output);
        # tab-delimited; the trivial word count is 1
        word = re.sub('[^a-zA-Z0-9]+', '', word.lower())
        print('%s,%s\t%s' % (word, filename, 1))
