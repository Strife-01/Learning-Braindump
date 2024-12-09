def quick_sort(left, right, array):
    print(left, right)
    if left < right:
        pivot = partition(left, right, array)
        quick_sort(left, pivot - 1, array)
        quick_sort(pivot + 1, right, array)

def partition(left, right, array):
    pivot = array[right]
    change_index = left
    # the pivot is the last element
    for i in range(left, right):
        if array[i] <= pivot:
            array[change_index], array[i] = array[i], array[change_index]
            change_index += 1
    array[change_index], array[right] = array[right], array[change_index]
    return change_index

def main():
    list_1 = [23,14,1234,123,5,1235,123,5,123,6,7,5,647,63,754,7,6,5468,5,796,5,48,76,32,5,2345,234,213,512,-3,5,-123,5,-123,5,-123,-5,123,-5,12,-3,51253]
    list_test = [23,14,1234,123,5,1235,123,5,123,6,7,5,647,63,754,7,6,5468,5,796,5,48,76,32,5,2345,234,213,512,-3,5,-123,5,-123,5,-123,-5,123,-5,12,-3,51253]
    quick_sort(0, len(list_1) - 1, list_1)
    assert list_1 == sorted(list_test)
    print(list_1)

if __name__ == "__main__":
    main()
