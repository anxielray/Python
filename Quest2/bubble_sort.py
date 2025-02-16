# write a function that implemenrs the bubble sort algorithm


def BubbleSort(nL):

    if sorted(nL):
        print("I was already sorted anyways!")
        return nL

    for i in range(len(nL) - 1):
        for j in range((i + 1), len(nL)):
            if nL[i] > nL[j]:
                nL[i], nL[j] = nL[j], nL[i]
            return nL


def sorted(nL):

    for i in range(len(nL) - 1):
        for j in range(i + 1, len(nL)):
            if nL[i] > nL[j]:
                return False
    return True


numbers = [1, 2, 3, 4, 5]
print(f"The list {numbers} when sorted becomes {BubbleSort(numbers)}")
