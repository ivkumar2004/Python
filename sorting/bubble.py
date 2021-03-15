"""
Bubble Sort Algorithm
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Implementing Bubble Sort Algorithm
Step 1: Starting with the first element(index = 0), compare the current element with the next element of the array.
Step 2: If the current element is greater than the next element of the array, swap them.
Step 3: If the current element is less than the next element, move to the next element. 
Step 4: Repeat Step 1, 2, 3.
"""


def bubbleSort(lstBubbleSort):
    n = len(lstBubbleSort) - 1 
    
    for i in range(n):
        for j in range(n-i):
            if( lstBubbleSort[j] > lstBubbleSort[j+1]):
                lstBubbleSort[j], lstBubbleSort[j+1] = lstBubbleSort[j+1], lstBubbleSort[j]
                
lstBubbleSort = [20,30,13,50,10,0]
bubbleSort(lstBubbleSort)
print(lstBubbleSort)