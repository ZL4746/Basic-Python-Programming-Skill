import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

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


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark







def header(input_type):
      
      header_string = "Input type = %s \n \
                    avg time   avg time   avg time \n \
   Sort function     (n=10)    (n=100)    (n=1000) \n \
-----------------------------------------------------\n "%(input_type)
      return header_string





def calculator(input_type, input_list_length, method):
      
      n = input_list_length
      timing = []
      for i in range (5):
            
            ########## Input type = Random ##########
            if input_type == "Random":
                  myList = [i for i in range(n)]
                  random.shuffle(myList)
            ########## Input type = Sorted ##########
            elif input_type == "Sorted":
                  myList = [i for i in range(n)]
            ########## Input type = Reverse ##########
            elif input_type == "Reverse":
                  myList = [i for i in range(n)]
                  myList = myList[::-1]
            ########## Input type = Almost sorted ##########
            elif input_type == "Almost sorted":
                  myList = [i for i in range(n)]
                  num_paird_to_swap = 0.1*n
                  swap_sucess = 0
                  while swap_sucess != num_paird_to_swap:
                        
                        randomIndex1 = random.randint(0,len(myList)-1)
                        randomIndex2 = random.randint(0,len(myList)-1)
                        if randomIndex1 != randomIndex2:
                              temp = myList[randomIndex1]
                              myList[randomIndex1] = myList[randomIndex2]
                              myList[randomIndex2] = temp
                              swap_sucess += 1
                              
                              
            startTime = time.perf_counter()
            if method == "bubbleSort":
                  bubbleSort(myList)
            elif method == "selectionSort":
                  selectionSort(myList)
            elif method == "insertionSort":
                  insertionSort(myList)
            elif method == "mergeSort":
                  mergeSort (myList)
            elif method == "quickSort":
                  quickSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            
            timing.append(elapsedTime)
            
      avg_time = (sum(timing)/ len(timing))
      
      return avg_time
      
      
      
def avg_time_list(input_type, sort_method):
      
      avg_time_list = []
      ########## n = 10 ##########
      avg_time = calculator(input_type, 10, sort_method)
      avg_time_list.append(avg_time)
      ########## n = 100 ##########
      avg_time = calculator(input_type, 100, sort_method)
      avg_time_list.append(avg_time)
      ########## n = 1000 ##########
      avg_time = calculator(input_type, 1000, sort_method)
      avg_time_list.append(avg_time)
      
      return avg_time_list



def statistics_output_string (input_type):
      
      
      ########## bubbleSort
      time_list1 = avg_time_list(input_type, "bubbleSort")
      bubbleSort    = "     bubbleSort    %.6f   %.6f   %.6f \n"%(time_list1[0],time_list1[1],time_list1[2])
      ########## selectionSort
      time_list2 = avg_time_list(input_type, "selectionSort")
      selectionSort = "   selectionSort    %.6f   %.6f   %.6f \n"%(time_list2[0],time_list2[1],time_list2[2])
      ########## insertionSort
      time_list3 = avg_time_list(input_type, "insertionSort")
      insertionSort = "   insertionSort    %.6f   %.6f   %.6f \n"%(time_list3[0],time_list3[1],time_list3[2])
      ########## mergeSort
      time_list4 = avg_time_list(input_type, "mergeSort")
      mergeSort     = "       mergeSort    %.6f   %.6f   %.6f \n"%(time_list4[0],time_list4[1],time_list4[2])
      ########## quickSort
      time_list5 = avg_time_list(input_type, "quickSort")
      quickSort     = "       quickSort    %.6f   %.6f   %.6f \n"%(time_list5[0],time_list5[1],time_list5[2])
      
      statistics_output = ( bubbleSort + selectionSort + insertionSort + mergeSort + quickSort)
      
      return statistics_output
      
      
      
def main():
      
      
      ########## Input type = Random ##########      
      random_output1 = header("Random")
      random_output1 += statistics_output_string("Random")
      print (random_output1)

      ########## Input type = Sorted ##########
      random_output2 = header("Sorted")
      random_output2 += statistics_output_string("Sorted")
      print (random_output2)
      
      ########## Input type = Reverse ##########
      random_output3 = header("Reverse")
      random_output3 += statistics_output_string("Reverse")
      print (random_output3)

      ########## Input type = Almost sorted ##########
      random_output4 = header("Almost sorted")
      random_output4 += statistics_output_string("Almost sorted")
      print (random_output4)

      
      
      
      
main()