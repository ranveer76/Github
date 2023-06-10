from insertion_sort import insertion_sort
def bucket_sort(x,z):
    bucket=[]
    slot=10
    for i in range(slot):
        bucket.append([])
    for j in x:
        index_b=int(slot*j)
        bucket[index_b].append(j)
    for i in range(slot):
        bucket[i]=insertion_sort(bucket[i],z)
    k=0
    for i in range(slot):
        for j in range(len(bucket[i])):
            x[k]=bucket[i][j]
            k+=1
    return x