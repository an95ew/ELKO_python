sequences = [12, 2, 2, 4, 1, 3, 1, 6, 8, 5, 2678, 67]


def my_filter(element):
    return element > 4


filtered_result = filter(my_filter, sequences)
print(filtered_result)

# lambda variant
filtered_result = filter(lambda x: x > 4, sequences)
print(list(filtered_result)
      )
