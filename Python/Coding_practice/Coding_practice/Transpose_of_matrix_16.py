m = [[2,4, 1,14],[3,4,5, 32],[5,6, 8, 91]] 



transpose = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


for i in transpose:
    print(i)
