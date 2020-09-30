animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana',
		'Giraffe', 'Elephant', 'Bear', 'Dog', 'Goose', 'Antelope', 'Zebra']

# Print all the animals

# How much longer is this going to take to run as the size of the data set
# increases?
#
# If we double it, twice as long
# If we halve it, half as long
# If we triple it, three times as long
#
# Linear time, O(n)

def print_animals():
	for a in animals:  # O(n) over the number of animals
		print(a)

def print_animal(i):   # O(1) over the number of animals
	print(animals[i])

# O(1) over the number of animals
# O(n) over the length of the string
def print_animal_2(i):
	for c in animals[i]:
		print(c)


"""
Steps for computing Big-O:

1. Wrote down the big O of each line in isolation
   * Loops get O(n)
   * Most other single lines get O(1)
2. Add the big O of things in series/sequence
3. Multiply the big O of each loop by its body

Also, drop constant multipliers.
Also, drop non-dominant terms in a sum.
"""

def find_dups():  # O(n^2)
	for i0 in range(len(animals)):     # n (over the number of animals)  O(n*n) O(n^2)
		for i1 in range(len(animals)):
			if i0 == i1:
				continue

			if animals[i0] == animals[i1]:
				print(f"Duplicate: {animals[i0]}")

def print_animals_3():

	# O(n + n) == O(2n) == O(n)

	for a in animals:
		print(a)

	for a in animals:
		print(a)


# Print a list of all possible animal triples
def print_animal_triples():  # O(n^3)
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print (f"{animal_1} - {animal_2} - {animal_3}")


"""
Better than O(n):
	O(log n)
	O(1)

Worse, but not bad:
	O(n log n)

Bad:
	O(n^2)
	O(n^3)
	O(2^n)
	O(n!)
"""

print_animals()
print_animal(3)
print_animal_triples()
print_animal_2(3)
print_animals_3()
find_dups()