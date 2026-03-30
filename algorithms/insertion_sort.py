def insertion_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(1, n):
        chave = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = chave

    return arr