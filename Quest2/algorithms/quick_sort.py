# Initialize global variable
B = []


def reorder(nL, pivot):
    global B  # Use the global variable B
    B.append(pivot)
    return B


def sorted(a):
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                return False
    return True


def resize(a):
    if len(a) <= 1:
        return a
    return a[1:]


def pivot(nL):
    return nL[0]


# QuickSort implementation
def quickSort(my_list):
    if len(my_list) <= 1:
        return my_list

    p = pivot(my_list)  # Get the pivot element
    smaller = [x for x in my_list[1:] if x <= p]
    larger = [x for x in my_list[1:] if x > p]

    return quickSort(smaller) + [p] + quickSort(larger)


if __name__ == "__main__":
    my_list = [100, 2, 87, 44, 5]
    print(
        f"Your list {my_list} when ordered using my quick sort becomes {quickSort(my_list)}"
    )
