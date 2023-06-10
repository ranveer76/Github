import array_importer as ai

importer=ai.importer

n=list(map(int,input().split()))
z=["ascending","descending"]
z1=int(input("Enter 1 for ascending or 2 for descending:\n"))
t=[
    "bubble_sort","selection_sort","insertion_sort",
   "merge_sort","quick_sort","heap_sort",
   "counting_sort","radix_sort","bucket_sort",
   "shell_sort","sequence_sort"
   ]

t1=int(
input("\nEnter 1 for bubble sort,2 for selection sort,\n"
      "3 for insertion sort,4 for merge sort,\n"
      "5 for quick sort,6 for heap sort,7 for counting sort,\n"
      "8 for radix sort,9 for bucket sort,10 for shell sort,\n"
      "11 for sequence sort:\n")
    )
x1=importer(t[t1-1])

x=x1(n,z[z1-1])
print(x)