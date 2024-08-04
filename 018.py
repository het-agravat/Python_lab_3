# 6. Perform Selection sorting given below elements. Elements[22,13,4,8,17,26,53,4]

def selection_sort(elements):
    for i in range(len(elements)):
        min_index = i
        for j in range(i + 1, len(elements)):
            if elements[j] < elements[min_index]:
                min_index = j
        elements[i], elements[min_index] = elements[min_index], elements[i]

elements = [22, 13, 4, 8, 17, 26, 53, 4]
selection_sort(elements)
print("Sorted elements:", elements)
