n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

if len(arr) != n:
    print("Error: Number of elements doesn't match n")
else:
    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print("Array after swapping adjacent elements:")
    print(*arr)
