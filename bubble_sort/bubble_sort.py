def bubble_sort(arr):
    # TODO: Implement bubble sort

    #An outer for loop to iterate through the array n times
    for n in range(len(arr)-1, 0, -1):
        #Initialize a boolean variable to track if any swaps occur
        swapped=False
        #Inner loop to compare adjacent elements in the array
        for i in range(n):
            if arr[i]> arr[i+1]:
                #Swap items if they are in the wrong order
                arr[i], arr[i+1]= arr[i+1], arr[i]
                swapped=True
        #If no swap occurs, the array is sorted
        if not swapped:
            break


arr=[56,34,45,71,16,7,9,90]
print("Unsorted array:\n", arr)

bubble_sort(arr)
print("Sorted array:\n", arr)

pass
