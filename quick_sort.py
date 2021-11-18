def quick_sort(sequence): #takes in a sequence of unsorted values
    length = len(sequence)
    if length <= 1:
        return sequence #allows algorithm to skip over sequences that have a length of one or zero
    else:
        pivot = sequence.pop()  #remove last element of sequence and return it

    items_greater = [] # items greater than pivot point
    items_lower = [] # items lower than pivot point

    for item in sequence: #compare each item left in sequence to pivot point
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater) #apply algorithm to sublists and concatonation of pivot point


print(quick_sort([1991, 1981, 1999, 2001, 2004, 2002, 1987, 1977, 1950, 1955, 1954, 1978]))

