def sorted_matrix_median(matrix, r, c):
    median_place = (r * c) // 2
    indices_reference= [0] * r
    i = 0
    min_value = float('inf')
    while i <= median_place:
        min_index, min_value = get_min_for_selected(matrix, indices_reference, c)
        i += 1
    return min_value


def get_min_for_selected(matrix, indices_reference, c):
    min_number = float('inf')
    min_index = 0
    for i in range(len(matrix)):
        if indices_reference[i] < c:
            row = matrix[i]
            if row[indices_reference[i]] < min_number:
                min_index = i
                min_number = row[indices_reference[i]]
    indices_reference[min_index] += 1
    return min_index, min_number


# print(sorted_matrix_median([[1, 3, 5], [2, 6, 9], [3, 6, 9]], 3, 3))
print(sorted_matrix_median([[1], [2], [3]], 3, 1))
