import pickle
import csv
from collections import deque
import time

t0 = time.clock()
adj_map = pickle.load(open('AdjMap.pickle', 'rb'))

textfile = open('output1.txt', 'w')


def bfs(a,b, adj_map):
    # make all necessary ques/lists

    visited = deque()
    que = deque()
    deg_dict = {}

    curr_node = a
    visited.append(curr_node)
    que.append(curr_node)
    deg_dict[curr_node] = 0


    while len(que) > 0:
        for i in adj_map[curr_node]:
            if i not in visited:
                que.append(i)
                visited.append(i)
                deg_dict[i] = deg_dict[curr_node] + 1
                if i == b:
                    return deg_dict[i]
                elif deg_dict[i] == 3:
                    return 3
            else:
                continue
        que.popleft()
        try:
            curr_node = que[0]
        except IndexError:
            return 0

'''
#TESTING GROUNDS###################
a = ' 28505'
b = ' 45177'

visited1 = bfs(a,b,adj_map)
visited2 = bfs(b,a,adj_map)

for i in visited1:
    if i in visited2:
        print('yay')
        break
###################################
'''


with open('stream_payment.csv', 'r', newline='', encoding='utf8') as csvfile:
    csvrd = csv.reader(csvfile, delimiter=',')
    for r in csvrd:
        if r[0] != 'time':
            try:
                a = r[1]
                b = r[2]
                degree = bfs(a,b,adj_map)

                if degree == 0 or degree == 3:
                    textfile.write(a+' '+ b +' '+ " Unverified\n")
                else:
                    textfile.write(a+' '+ b +' '+ " Verified Friend\n")
            except IndexError:
                continue
        else:
            continue

t1 = time.clock()

totaltime = t0-t1

textfile.write('\n' + totaltime + '\n')
textfile.close()



