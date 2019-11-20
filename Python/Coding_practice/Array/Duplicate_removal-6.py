array=[2,3,23,5,6,2,234,5,2,5,6,4,23,2]

lst = []

for i in  array:
      if i not in lst:
              lst.append(i)

print(lst)
