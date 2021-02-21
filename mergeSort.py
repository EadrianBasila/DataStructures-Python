import sys

def mergeSort(num):
	mergeSortB(num, 0, len(num)-1)
	
def mergeSortB(num, firstPart, lastPart):
	if firstPart < lastPart:
		middlePart = (firstPart + lastPart)//2
		mergeSortB(num, firstPart, middlePart)
		mergeSortB(num, middlePart+1, lastPart)
		merge(num, firstPart, middlePart, lastPart)
		
def merge(num, firstPart, middlePart, lastPart):
	L = num[firstPart:middlePart+1]
	R = num[middlePart+1:lastPart+1]
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	i = j = 0
	
	for k in range (firstPart, lastPart+1):
		if L[i] <= R[j]:
			num[k] = L[i]
			i += 1
		else:
			num[k] = R[j]
			j += 1

def main():
    			
    print("[Please Enter Numbers Separated by Comma]")
    nums = input("Enter numbers:\n").split(',')
    numsList = [int(n) for n in nums]

    mergeSort(numsList)
    print("*"*35)
    print("Merge Sorted Numbers: ")
    print(numsList)
    print("*"*35)

main()