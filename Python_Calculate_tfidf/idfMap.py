#!/usr/bin/env python
# Revised by Parke Godfrey
# 2017-09-24

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    print('%s' % (line))

    word = re.sub(',[\S\t]+', '', line)
    print('%s\t%s' % (word, 1))
