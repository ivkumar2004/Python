#To generate the prime numbers between the given numbers
import re

#Get the numbers from user
rangeStart = (input("Please enter the starting number: ")).strip()
rangeEnd = input("Please enter the last number: ")

#Validating the given input is number
matchGroup = re.match("^\d+$",rangeEnd)
if not matchGroup:
    print("Only digits accepted for validation: " + rangeEnd)
    exit()
    
matchGroup = re.match("^\d+$",rangeStart)
if not matchGroup:
    print("Only digits accepted for validation: " + rangeStart)
    exit()

#Check the number is in assending    
num1 = int(rangeStart)
num2 = int(rangeEnd)

if num1>num2:
    num1, num2 = num2, num1
    
print (num1, num2)

#Generating prime number
for number in range(num1,num2+1):
    if number < 3:
        print ("Prime number: ",number)
        continue
        
    for validateNumber in range(2,int(number/2)+1):
        if number%validateNumber == 0:
            break
    else:
        print("Prime number: ",number)