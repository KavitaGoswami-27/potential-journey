
def is_nearly_sorted(arr):
    if len(arr) < 2:
        return True
    count = sum(1 for i in range(len(arr) - 1) if arr[i] > arr[i + 1])
    return count <= max(1, len(arr) * 0.1) 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = merge_sort(arr[:mid])
        R = merge_sort(arr[mid:])
        result = []
        i = j = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                result.append(L[i])
                i += 1
            else:
                result.append(R[j])
                j += 1
        result += L[i:]
        result += R[j:]
        return result
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def counting_sort(arr):
    if not arr or not all(isinstance(x, int) and x >= 0 for x in arr):
        raise ValueError("Counting sort works only with non-negative integers.")
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i, c in enumerate(count):
        sorted_arr.extend([i] * c)
    return sorted_arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def intelligent_sort(arr):
    original = arr.copy()
    arr_type = "Quick Sort"
    
    if len(arr) <= 5:
        sorted_arr = selection_sort(arr)
        arr_type = "Selection Sort"
    elif len(arr) <= 10:
        sorted_arr = insertion_sort(arr)
        arr_type = "Insertion Sort"
    elif is_nearly_sorted(arr):
        sorted_arr = bubble_sort(arr)
        arr_type = "Bubble Sort (Nearly Sorted)"
    elif all(isinstance(x, int) and x >= 0 for x in arr) and len(set(arr)) < len(arr) * 0.5:
        sorted_arr = counting_sort(arr)
        arr_type = "Counting Sort"
    elif len(arr) > 20:
        sorted_arr = merge_sort(arr)
        arr_type = "Merge Sort"
    elif len(arr) > 15:
        sorted_arr = heap_sort(arr)
        arr_type = "Heap Sort"
    else:
        sorted_arr = quick_sort(arr)

    return {"sorted": sorted_arr, "algorithm": arr_type}
