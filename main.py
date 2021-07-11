def main(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

num_input = input("Enter numbers: ")
arr = [int(x) for x in num_input.split()]

main(arr)

print("Sorted array:")
for i in range(len(arr)):
    print(arr[i])