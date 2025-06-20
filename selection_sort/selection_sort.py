def selection_sort(array, size):
    # TODO: Implement selection sort

        for POS in range(size):
            smallest=POS

            for j in range(POS + 1, size):
                # selecting the smallest element in every iteration
                if array[j] < array[smallest]:
                    smallest = j
            # swapping the elements to sort the array
            (array[POS], array[smallest]) = (array[smallest], array[POS])

arr = [2, 9, 7, 11, 31, 18, -9]
print("Unsorted array:\n", arr)

size = len(arr)
selection_sort(arr, size)
print('Sorted array:')
print(arr)