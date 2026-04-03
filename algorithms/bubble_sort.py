def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # troca
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr