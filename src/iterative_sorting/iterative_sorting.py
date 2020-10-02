list_to_sort = [16, 19, 11, 15, 10, 12, 14, 20, 30, 40, 90, 50, 60, 70,
                80, 100, 110, 7, 234, 34, 76, 309, 22, 54, 26, 93, 17,
                77, 31, 44, 55, 20]


def selection_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
        if least is not i:
            collection[least], collection[i] = (collection[i],
                                                collection[least])
    return collection


def bubble_sort(collection):
    for pass_num in range(len(collection)-1, 0, -1):
        for i in range(pass_num):
            if collection[i] > collection[i + 1]:
                t = collection[i]
                collection[i] = collection[i+1]
                collection[i+1] = t
    return collection


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here
    pass
