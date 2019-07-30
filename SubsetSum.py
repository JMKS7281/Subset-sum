#Program is developed by Janmanchi Mohana Krishna
#This code is to find the minimum elements from the given array to form required sum
#Email: jmks.8008@gmail.com
#Phone: 9491007517

def powerset(s,k):
    result=[]   #array to store all powerset
    subset=[]   #array to store subsets which forms the required sum
    resultLength=[] #array to store length of each obtained subset
    length=len(s)

    #finding powersets
    for i in range(1<<length):
        result.append([s[j] for j in range(length) if (i&(1<<j))])
    #print(result)  #---->this is to find powerset of a given set
    try:

        #finding the subsets forming required sum from the powerset 
        for i in range(len(result)):
            if(sum(result[i])==k):
                subset.append(result[i])    #subset storing  
                resultLength.append(len(result[i])) #length of subset storing
        print(subset[resultLength.index(min(resultLength))],end=' ')    #printing the subset with minimum number of elements
        print("are the Minimum elements to find required sum")
    except:
        print("No subset from given set can form required sum")
    
            
#taking the Input Array of elements
arr=[10,0,-1,20,25,30]

#Taking the required sum and storing
print("Enter the Required sum")
reqsum=int(input())

#calling the function
powerset(arr,reqsum)
