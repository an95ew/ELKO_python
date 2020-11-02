sequences = [12, 2, 2, 4, 1, 3, 1, 6, 8, 5, 2678, 67]

ptr_next = map(lambda number: number * number, filter(lambda number: number > 4, sequences))
print(set(ptr_next))
