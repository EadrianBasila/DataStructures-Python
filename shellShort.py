def shellSort(numsList): 
  n = len(numsList)
  num = n // 2 
  while num > 0: 
    for i in range(num,n): 
      temp = numsList[i] 
      j = i 
      while  j >= num and numsList[j-num] > temp: 
        numsList[j] = numsList[j-num] 
        j = j - num 
      numsList[j] = temp 
    num = num // 2

  

def main():
    			
    print("[Please Enter Numbers Separated by Comma]")
    nums = input("Enter numbers:\n").split(',')
    numsList = [int(n) for n in nums]

    shellSort(numsList)
    print("*"*35)
    print("Shell Sorted Numbers: ")
    print(numsList)
    print("*"*35)

main()