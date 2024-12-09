l = [ 50 , 31 , 21 , 28 , 72 , 41 , 73 , 93 , 68 , 43 , 45 , 78 , 5 , 17 , 97 , 71 , 69 , 61 , 88]


def main() -> None:
    # needed variables
    left: int = 0
    right: int = len(l) - 1

    # print unsorted list
    print(l)
    # sort the list
    merge_sort(l, left, right)
    # print sorted list
    print(l)


def merge_sort(l, left: int, right: int) -> None:
    # if the list is not sorted
    if left < right:
        mid: int = int((left + right) / 2)
        # sort the left side
        merge_sort(l, left, mid)
        # sort the right side
        merge_sort(l, mid + 1, right)
        # merge them together
        merge(l, left, mid, right)
    else:
        return


def merge(l, left: int, mid: int, right: int) -> None:
    # Create a temp list with the left content
    left_list = l[left: mid + 1]
    # Create a temp list with tht right content
    right_list = l[mid + 1:right + 1]
    # Reintroduce the items in the first list
    i: int = 0
    j: int = 0
    k: int = left
    limit: int = len(l)
    while k < limit and i != len(left_list) and j != len(right_list):
        if left_list[i] <= right_list[j]:
            l[k] = left_list[i]
            i += 1
            k += 1
        else:
            l[k] = right_list[j]
            j += 1
            k += 1
    # Copy the remaining elements in the left list
    while i < len(left_list):
        l[k] = left_list[i]
        i += 1
        k += 1

    # Copy the remaining elements in the right list
    while j < len(right_list):
        l[k] = right_list[j]
        j += 1
        k += 1


if __name__ == "__main__":
    main()
