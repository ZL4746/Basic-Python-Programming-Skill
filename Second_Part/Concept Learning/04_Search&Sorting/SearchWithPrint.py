def bubbleSort(alist):
    for passnum in range(1,len(alist)):
        print("Pass",passnum)
        for i in range(1,len(alist)):
            if alist[i-1] > alist[i]:
                print("Switch",alist[i-1],"and",alist[i])
                temp = alist[i]
                alist[i] = alist[i-1]
                alist[i-1] = temp
            else:
                print("Don't switch",alist[i-1],"and",alist[i])

        print(alist)
        dummy = input("")


def shortBubbleSort(alist):
    exchangesThisPass = True
    passnum = 1

    while passnum <= len(alist) and exchangesThisPass:
        print("Pass",passnum)
        exchangesThisPass = False
        for i in range(1,len(alist)-passnum+1):
            if alist[i-1] > alist[i]:
                print("Switch",alist[i-1],"and",alist[i])
                exchangesThisPass = True
                temp = alist[i]
                alist[i] = alist[i-1]
                alist[i-1] = temp
            else:
                print("Don't switch",alist[i-1],"and",alist[i])
        print(alist)
        dummy = input("")
        passnum += 1


def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        print("Max from 0 to",fillslot,"is",alist[positionOfMax])
        print("Swapping with",alist[fillslot])
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
        print(alist)
        dummy=input("")


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        print("Assuming",alist[:position],"is sorted")
        print("Inserting",currentvalue)
        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue
        print(alist)
        dummy=input("")

    
def mergeSort(alist):

    print("Sorting ",alist)
    dummy=input("")

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        print("Recursive call on left half")
        mergeSort(lefthalf)
        print("Recursive call on right half")
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        print("merging",lefthalf,"and",righthalf)
        dummy=input("")
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

        print("result of merge:",alist)
        dummy=input("")


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)


def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        print("recursive call: sort left sublist from",alist[first],"to",alist[splitpoint-1])
        quickSortHelper(alist,first,splitpoint-1)
        print("recursive call: sort right sublist from",alist[splitpoint+1],"to",alist[last])
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]
    print("pivot =",pivotvalue)
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        print("   item bigger than pivot:",alist[leftmark],", item smaller than pivot:",alist[rightmark])
        if rightmark < leftmark:
            print("   crossover:  done with pass")
            done = True
        else:
            print("   swapping",alist[leftmark],"and",alist[rightmark])
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            print("   list now: ",alist)
            dummy=input("")

    print("   moving pivot: swapping",alist[first],"and",alist[rightmark])
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    print("   list now: ",alist)
    dummy=input("")

    return rightmark


def main():

    # original list
    myList = [54,26,93,17,77,31,44,55,20]

    # mostly sorted
    #myList = [17,20,26,93,54,77,31,44,55]

    print("Initial list: ", myList)
    # edit the following line with the sort routine you want to run
    mergeSort(myList)
    print("Final list: ",myList)

main()

