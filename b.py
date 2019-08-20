list1=[1,2,4,3]
def bubblesort(list1):
    for passnum in(len(list1)-1,0,-1):
        for i in range(passnum):
            if(list1[i]>=list1[i+1]):
                temp=list1[i]
                list1[i]=list1[i+1]
                list1[i+1]=temp
    print(list1)
