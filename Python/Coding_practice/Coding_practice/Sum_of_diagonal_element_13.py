lst = [[1, 9, 11,3], [10, 4,11, 20], [2, 8, 10, 11]]




def Diagonal_sum_diiference(lst):
    
    reverse_lst = []
    diagonal = []

    reverse_diagonal = []

    for i in range(len(lst)):
        x=lst[i][i]

        diagonal.append(x)
        reverse_lst.append(lst[i][::-1])


    for j in range(len(reverse_lst)):
        y = reverse_lst[j][j]
        reverse_diagonal.append(y)

    #print(sum(diagonal))
    #print(sum(reverse_diagonal))


    x = abs(sum(diagonal)- sum(reverse_diagonal))
    print(reverse_lst)
    return x





print(Diagonal_sum_diiference(lst))
