import pandas as pd
import csv
import pickle
from collections import deque, defaultdict

# initialize some variables
pickle_out = open('AdjMap.pickle', 'wb')  # this is where we want to store our adjMatrix
dic = defaultdict(list)  # adjacency matrix is basically a python dictionary holding adjacent friends


with open('batch_payment.csv','r', newline='', encoding='utf8') as csvfile:
    csvrd = csv.reader(csvfile, delimiter=',')
    for r in csvrd:

            if r[0] != 'time':
                try:
                    a = r[1]
                    b = r[2]
                    if b not in dic[a]:
                        dic[a].append(b)
                        dic[b].append(a)
                    else:
                        continue
                except IndexError:
                    continue
            else:
                continue


'''
with open('stream_payment.csv', 'r') as csvfile:
    csvrd = csv.reader(csvfile, delimiter=',')
    i = 0
    for r in csvrd:
        while i <= 20:
            print(r)
            isthere = degreerangelookup(r[1], r[2])
            if isthere==False:
                print("unverified")
            else:
                print("trusted")
            ++i
'''


# store the adjacency matrix in byte format for future streams


pickle.dump(dic, pickle_out)
pickle_out.close()