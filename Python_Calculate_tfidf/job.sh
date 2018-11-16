#!/bin/bash

WCDIR=/home/tfidf
STREAMINGJAR=share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar

printf "TF MAP-REDUCE\n\n"
bin/hadoop jar $STREAMINGJAR                        \
    -files   $WCDIR/tfMap.py,$WCDIR/tfReduce.py \
    -mapper  $WCDIR/tfMap.py                      \
    -reducer $WCDIR/tfReduce.py                   \
    -input   projectdata/word-test/'*'                          \
    -output  TF
    
printf "\nIDF MAP-REDUCE\n\n"
bin/hadoop jar $STREAMINGJAR                            \
    -files   $WCDIR/idfMap.py,$WCDIR/idfReduce.py \
    -mapper  $WCDIR/idfMap.py                        \
    -reducer $WCDIR/idfReduce.py                     \
    -input   TF/'*'                                   \
    -output  IDF

printf "\nFINAL OUTPUT\n\n"
bin/hadoop fs -cat IDF/part-00000 > $WCDIR/word-test.txt

bin/hadoop fs -rm -r TF
bin/hadoop fs -rm -r IDF

