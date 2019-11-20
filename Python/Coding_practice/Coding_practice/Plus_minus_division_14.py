list1 = [-4 ,3 ,-9 ,0 ,4 ,1  ]


def plus_minus(list1):

    pos = 0
    neg = 0
    zero = 0

    for i in list1:
        if i>0:
            pos +=1
        elif i<0:
            neg  += 1
        elif i==0:
            zero +=1


    postitive_value = float(pos/len(list1))
    negative_value = float(neg/len(list1))
    zero_value = float(zero/len(list1))

    x = format(postitive_value, '.6f')
    y = format(negative_value, '.6f')
    z = format(zero_value, '.6f')

    print(x)
    print(y)
    print(z)


plus_minus(list1)
