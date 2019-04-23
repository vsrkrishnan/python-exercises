
arr = [8, 7, 2, 5, 3, 1]

total = 10

def findPair(arr, total):
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low < high:
        if arr[low] + arr[high] == total:
            print "Pair found at indexes {} and {}".format(low, high)
            return

        if arr[low] + arr[high] < total:
            low += 1
        else:
            high -= 1

    print "Pair not found."

findPair(arr, total)

