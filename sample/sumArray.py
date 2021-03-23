import os
import sys
import functools

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    return functools.reduce(lambda x,y:x+y, ar)
    sum = 0
    for number in ar:
        sum += number
    return sum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    #fptr.write(str(result) + '\n')
    #fptr.close()
    print(result)
