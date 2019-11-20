def findLongestConseqSubseq(arr): 
  
    s = set() 
    ans=0
    n= len(arr)
    for ele in arr: 
        s.add(ele) 
    for i in range(n): 
        if (arr[i]-1) not in s: 
           
            j=arr[i] 
            while(j in s): 
                j+=1
            ans=max(ans, j-arr[i]) 
    return ans 

lst = [1, 9, 3, 10, 4, 20, 2]

print(findLongestConseqSubseq(lst)) 