#!/bin/sh

# A Bourne shell script that takes a number of input text 
# files and converts each of the files into a list of words.
# It calls extractwords.sh to convert each file listed in
# the command line into a list of words and outputs the 
# list of words for a file into a new file with ".words" 
# extension.
#
# An example usage: extractmultfiles.sh course/*
# It takes as input all the files under the directory "course" 
# and outputs the lists of words into course/*.words files.

# Check usage
if [ $# -lt 1 ]
then
  echo "Usage: $0 <a list of text files>" 1>&2
  exit 1
fi

for x in $*  # $* contains all command-line arguments 
do
  sh extractwords.sh $x > $x.words 
done
