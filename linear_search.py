# O(n log n) 

animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana',
		'Giraffe', 'Elephant', 'Bear', 'Dog', 'Goose', 'Antelope']


animals.sort()   # O(n log n)

"""
Binary search drops half the search space each iteration.

Any time you drop half the data each step, you should be thinking "This is O(log n)".

['Aardvark', 'Antelope', 'Bear', 'Cat', 'Dog', 'Duck', 'Elephant', 'Flamingo', 'Giraffe', 'Goose', 'Hippo', 'Iguana', 'Jackal']
['Aardvark', 'Antelope', 'Bear', 'Cat', 'Dog', 'Duck']
['Aardvark', 'Antelope', 'Bear']
['Bear']
"""

def binary_search(arr, target):  # O(log n)
    low = 0
    high = len(arr) - 1
    print(low, high)
    middle = int((low + high) / 2)
    print(arr[middle])
    while low <= high:
        middle = int((low + high) / 2)
        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return middle
    return -1

# Linear search, O(n) over number of animals
def find_animal(a):
    for animal in animals:
        if animal == a:
            return True

    return False

# print(find_animal("Goose"))
# print(find_animal("Rockfish"))

print(binary_search(animals, "Goose"))
print(binary_search(animals, "Rockfish"))
