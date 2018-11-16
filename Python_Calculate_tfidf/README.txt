READ ME
This program is a MapReduce work for Hadoop to find the tf-idf of words among all the document of the file.
Can run the program by just:
bash# cd /usr/local/hadoop
bash# sh /home/tfidf/job.sh 2>&1 | tee /home/runLog

Instruction:
We write two Map-reduce procedures.
	1. tfMap.py & tfReduce.py: calculate the TF number for each (word, document) key, that is number of occurrence of word in document
	2. idfMap.py & idfReduce.py: calculate the IDF number and TF-IDF score for each word key. One note is that for this project: the total number of the document in the folder is constant: 463 in training data and 206 in the testing.
	3. Store the outputs into /home/projectdata/final.txt.

The procedure for you to invoke this program:
	1. open the Docker on you laptop. (this is the container for the Hadoop)
``	2. open the terminal type the following words to start the docker
		mybox% docker start Hadoop
	3. then copy the file from the computer home filesystem to the docker container
		mybox% docker cp projectdata Hadoop:/home/projectdata
	4. to get the bash shell within the container type
		mybox% docker attach Hadoop
	5. if you want to check if the file you put inside is already inside the container, type 	bash$ bin/hadoop fs -ls 
	6. copy the input file to Hadoop's hfs filesystem type:
		bash$ bin/hadoop fs -put /home/projectdata/word-train word-train
	7. to excuse the Hadoop MapReduce job, run the shell file
		bash# cd /usr/local/hadoop
		bash# sh /home/projectdata/job.sh 2>&1 | tee /home/runLog

