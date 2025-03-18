def divide_and_conquer(arr, left, right):
    if left == right:
        return arr[left], arr[left]

    if right - left == 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]

    mid = (left + right) // 2
    min1, max1 = divide_and_conquer(arr, left, mid)
    min2, max2 = divide_and_conquer(arr, mid + 1, right)

    return min(min1, min2), max(max1, max2)


def find_min_max(arr):
    if not arr:
        raise ValueError("Масив не може бути порожнім")

    return divide_and_conquer(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [4, 22, 12, 6, 9, 11, 15, 8]
    print(find_min_max(arr))
