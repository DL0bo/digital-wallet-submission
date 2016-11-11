import pickle
import csv
from collections import deque
import os

cur_path = os.path.dirname(__file__)
to_path = os.path.relpath('..\\paymo_output\\output1.txt')
from_path = os.path.relpath('..\\paymo_input\\stream_payment.csv')

rows = 0
adj_map = pickle.load(open('AdjMap.pickle', 'rb'))

textfile = open(to_path, 'w')


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
                elif deg_dict[i] == 2:
                    return 2
            else:
                continue
        que.popleft()
        try:
            curr_node = que[0]
        except IndexError:
            return 0




with open(from_path, 'r', newline='', encoding='utf8') as csvfile:
    csvrd = csv.reader(csvfile, delimiter=',')
    for r in csvrd:

        if rows == 500:
            break
        if r[0] != 'time':
            try:
                a = r[1]
                b = r[2]
                degree = bfs(a,b,adj_map)

                if degree == 0 or degree == 2:
                    textfile.write("unverified: You've never had a transaction with user: "+ b + " before. Are you sure you would like to proceed with this payment?"+"\n")
                else:
                    textfile.write(a+'\'s Money transferred to '+ b +' '+ "\n")
            except IndexError:
                continue
        else:
            continue
        rows += 1


textfile.close()



