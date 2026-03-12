#need to open and close files to read data
fp = open(path)
for line in fp:
    do_something(line)
fp.close()

#compressed files
import gzip
with gzip.open(path, 'rt') as fp:
    for line in fp:
        print(line, end='')

#to step through FASTA files

import sys
import (library)

for defline, seq in (library).read_fasta(sys.argv[1]):
    print(defline[:30], seq[:40], len(seq))
    
#sliding window algorithm
w = 10  #size of window
s = 1   #step size
for i in range(0, len(seq) -w +1, s):   #move window along without allowing runoff
    subseq = seq[i:i+w]   #creats slice using offset

#dictionaries
d = {}  #or
d = dict()

d = {'key': 'value', 'key': 'value'}

