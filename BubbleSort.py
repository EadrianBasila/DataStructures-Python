def bubbleSort(num):
	for i in range (0, len(num) - 1):
		done = True
		for b in range (0, len(num) - i - 1):
			if num[b] > num[b+1]:
				num[b], num[b+1] = num[b+1], num[b]
				done = False
		if done:
			return

def main():
    			
    print("[Please Enter Numbers Separated by Comma]")
    nums = input("Enter numbers:\n").split(',')
    numsList = [int(n) for n in nums]


    bubbleSort(numsList)
    print("*"*35)
    print("Bubble Sorted Numbers: ")
    print(numsList)
    print("*"*35)

main()