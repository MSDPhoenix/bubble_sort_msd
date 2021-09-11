x=[5,1,4,2,8,9,8,7,6,4,5,3,2,1]
y=[5,1,4,2,8]

def bubble_sort(bbl):
        finished=0
        count=0
        while finished!=len(bbl)-1:
            finished=0
            for i in range(len(bbl)-1):
                count+=1
                if bbl[i]>bbl[i+1]:
                    bbl[i],bbl[i+1]=bbl[i+1],bbl[i]
                else:
                    finished+=1
        print(count,"comparisons")
        print(bbl) 

bubble_sort(y)
bubble_sort(x)




x=[5,1,4,2,8,9,8,7,6,4,5,3,2,1]
y=[5,1,4,2,8]

def bubble_sort(bbl):
    count=0
    for j in range(len(bbl)-1):
        for i in range(len(bbl)-1-j):
            count+=1
            if bbl[i]>bbl[i+1]:
                bbl[i],bbl[i+1]=bbl[i+1],bbl[i]
    print(count,"comparisons")
    print(bbl)

bubble_sort(y)
bubble_sort(x)