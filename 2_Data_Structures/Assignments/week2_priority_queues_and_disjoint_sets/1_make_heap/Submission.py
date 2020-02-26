# python3

# Problem 1 Array into Heap
def min_heapify(arr):
    swaps_list = []
    swaps = 0
    end = len(arr) - 1
    last_parent = (end - 1) // 2
    # Iterate from last parent to first
    for parent in range(last_parent, -1, -1):
        current_parent = parent
        # Iterate from current_parent to last_parent
        while current_parent <= last_parent:
            # Find lesser child of current_parent
            child = 2 * current_parent + 1
            if child + 1 <= end and arr[child] > arr[child + 1]:
                   child = child + 1
            # Swap if child is less than parent
            if arr[child] < arr[current_parent]:
                swaps += 1
                arr[current_parent], arr[child] = arr[child], arr[current_parent]
                swaps_list.append((current_parent,child))
                current_parent = child
            # If no swap occured, no need to keep iterating
            else:
                break
    return swaps, swaps_list

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps, swaps_list = min_heapify(data)
    print(swaps)
    for i, j in swaps_list:
        print(i, j)

if __name__ == "__main__":
    main()
