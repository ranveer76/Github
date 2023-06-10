# Purpose: Array class for sorting algorithms
def importer(x):
    if x=="bubble_sort":
        from sorting.bubble_sort import sort
    elif x=="insertion_sort":
        from sorting.insertion_sort import insertion_sort as sort
    elif x=="selection_sort":
        from sorting.selection_sort import selection_sort as sort
    elif x=="sequence_sort":
        from sorting.sequence_sort import sequence_sort as sort
    elif x=="merge_sort":
        from sorting.merge_sort import merge_sort as sort
    elif x=="quick_sort":
        from sorting.quick_sort import quick_sort as sort
    elif x=="heap_sort":
        from sorting.heap_sort import heap_sort as sort
    elif x=="counting_sort":
        from sorting.counting_sort import counting_sort as sort
    elif x=="radix_sort":
        from sorting.radix_sort import radix_sort as sort
    elif x=="bucket_sort":
        from sorting.bucket_sort import bucket_sort as sort
    else:
        from sorting.shell_sort import shell_sort as sort
    return sort
def print_list():
    t=[
    "bubble_sort","selection_sort","insertion_sort",
   "merge_sort","quick_sort","heap_sort",
   "counting_sort","radix_sort","bucket_sort",
   "shell_sort","sequence_sort"
   ]
    return t

    