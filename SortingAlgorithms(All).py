#Make a Menu for All Programm
import time
import os
import sys 


CarGarageStackSystem = [] 
ArrivalStack = 0
DepartalStack = 0

CarGarageQueueSystem = [] 
ArrivalQueue = 0
DepartalQueue = 0

count = 0
class Node(object):
    
	def __init__ (self, d, n = None):
		self.data = d
		self.next_node = n

	def get_next (self):
		return self.next_node

	def set_next (self, n):
		self.next_node = n
		
	def get_data (self):
		return self.data

	def set_data (self, d):
		self.data = d
		
	def has_next (self):
		if self.get_next() is None:
			return False
		return True
		
	def to_string (self):
		return "Node value: " + str(self.data)

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right		

class LinkedList (object):

	def __init__ (self, r = None):
		self.root = r
		self.size = 0

	def get_size (self):
		return self.size

	def add (self, d):
		new_node = Node (d, self.root)
		self.root = new_node
		self.size += 1

	def add_node (self, n):
		n.set_next(self.root)
		self.root = n
		self.size += 1
		
	def removeElement (self, d):
		this_node = self.root
		prev_node = None

		while this_node is not None:
			if this_node.get_data() == d:
				if prev_node is not None:
					prev_node.set_next(this_node.get_next())
				else:
					self.root = this_node.get_next()
				self.size -= 1
				return True     # data removed
			else:
				prev_node = this_node
				this_node = this_node.get_next()
		return False  # data not found

	def findElement (self, d):
		this_node = self.root
		while this_node is not None:
			if this_node.get_data() == d:
				return d
			elif this_node.get_next() == None:
				return False
			else:
				this_node = this_node.get_next()
				
	def print_list (self):
		if self.root is None:
			return
		this_node = self.root
		print (this_node.to_string())
		while this_node.has_next():
			this_node = this_node.get_next()
			print (this_node.to_string())
			
	def sortElements (self):
		if self.size > 1:
			newlist = [];
			current = self.root;
			newlist.append(self.root);
			while current.has_next():
				current = current.get_next();
				newlist.append(current);
			newlist = sorted(newlist, key = lambda node: node.get_data(), reverse = True);
			newll = LinkedList();
			for node in newlist:
				newll.add_node(node);
			return newll;
		return self;

# Function to perform inorder traversal on the BST
def inorder(root):
 
    if root is None:
        return
 
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
 
 
# Function to find the maximum value node in the subtree rooted at `ptr`
def maximumKey(ptr):
 
    while ptr.right:
        ptr = ptr.right
    
    return ptr
 
 
# Recursive function to insert a key into a BST
def insert(root, key):
 
    # if the root is None, create a new node and return it
    if root is None:
        print("{} has been added as a new node of the tree".format(key))
        return Node(key)
 
    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        print("{} has been inserted to the left subtree.".format(key))
        root.left = insert(root.left, key)
 
    # if the given key is more than the root node, recur for the right subtree
    else:
        print("{} has been inserted to the right subtree.".format(key))
        root.right = insert(root.right, key)
 
    return root
 
 
# Function to delete a node from a BST
def deleteNode(root, key):
 
    # base case: the key is not found in the tree
    if root is None:
        print("[!]Element not found on Tree.")
        return root

    if key < root.data:
        root.left = deleteNode(root.left, key)
        

    elif key > root.data:
        root.right = deleteNode(root.right, key)
 
    # key found
    else:

        if root.left is None and root.right is None:

            print("[#]Node has no children.")
            return None
 
        elif root.left and root.right:
            print("[#]Node has children on both sides.")

            predecessor = maximumKey(root.left)

            root.data = predecessor.data
 
            root.left = deleteNode(root.left, predecessor.data)
            print("[-] Deleting Node.")

        else:
            print("[#]Node has children.")

            child = root.left if root.left else root.right
            root = child
        print("[-] {} element deleted.".format(key))

    return root
    
def printOption():
    print("-="*18)
    print("Binary Search Tree")
    print("1.) Add elements to the tree")
    print("2.) Delete elements to the tree")
    print("3.) Exit")
    print("-="*18)

def LinkedList ():
	    myList = LinkedList()
	    option = 0
	    while(option != 4):
			    print("")
			    print("-="*18)
			    print("Linked List")
			    print("1.) Add elements to the list")
			    print("2.) Delete elements to the list")
			    print("3.) Find elements in the list")
			    print("4.) Exit")
			    print("-="*18)
			    option = int(input("Enter your Choice: "))
			

			    if (option == 1):
				    print("")
				    print("[Please Enter Numbers Separated by Comma]")
				    nums = input("Enter numbers:\n").split(',')
				    keys = [int(num) for num in nums]
				
		
				    for key in keys:
					    myList.add(key)
				
				    myList = myList.sortElements()
				    print("size="+str(myList.get_size()))
				    print("*"*35)
				    myList.print_list()
				    print("*"*35)

			    elif (option == 2):
				    print("[Please Enter the Number to be Deleted]")
				    numDel = int(input("Enter Number: "))
				    myList.removeElement(numDel)
				    myList = myList.sortElements()
				    print("size="+str(myList.get_size()))
				    print("*"*35)
				    myList.print_list()
				    print("*"*35)
			
			    elif (option == 3):
				    print("[Please Enter the Number to Find]")
				    numFind = int(input("Enter Number: "))
				    findBool = myList.findElement(numFind)
				    if findBool == numFind:
					    print("Element[{}] is on the list.".format(numFind))
				    else:
					    print("Element[{}] is not on the list.".format(numFind))
			
			    elif (option == 4): break
			    else: print("[!]Please choose from options above.")
def AddCarStack():
        global ArrivalStack
        global DepartalStack 
        global CarGarageStackSystem
        print("Remaining park slot: " + str(10-len(CarGarageStackSystem)))
        PlateNumberofCar = input("Please provide the platenumber of your car: ")
        CarGarageStackSystem.append(PlateNumberofCar)
        time.sleep(3)
        print("Car Arriving: " + PlateNumberofCar)
        print(str(CarGarageStackSystem))
        time.sleep(2)
        print("Remaining park slot: " + str(10-len(CarGarageStackSystem)))
        ArrivalStack +=1
        print("Number of arrivals happened: " + str(ArrivalStack))
        print("Number of departals happened: " + str(DepartalStack))

def RemoveCarStack():
    global ArrivalStack
    global DepartalStack
    print("Here is the list of cars",  CarGarageStackSystem)
    CarGarageStackSystem.reverse()
    Remove = input("What car do you want to remove? ")
    IndexToBeRemove = int(CarGarageStackSystem.index(Remove))
    if Remove in CarGarageStackSystem:
        i = 0
        while i < IndexToBeRemove+1:
            print("Now Departing: " + str(CarGarageStackSystem[i]))
            DepartalStack += 1
            i+=1
            time.sleep(3)
        print("All cars will start to move back in the garage")
        time.sleep(5)
        j=0
        CarGarageStackSystem.reverse()
        CarGarageStackSystem.remove(Remove)
        while j < IndexToBeRemove:
            print("Now Arriving: " + str(CarGarageStackSystem[j]))
            ArrivalStack +=1
            j+=1
            time.sleep(3)
        time.sleep(3)
    print("Number of arrivals happened: " + str(ArrivalStack))
    print("Number of departals happened: " + str(DepartalStack))

def BubbleSort():

    while True:
        def bubbleSort(num):
            for i in range (0, len(num) - 1):
                done = True
                for b in range (0, len(num) - i - 1):
                    if num[b] > num[b+1]:
                        num[b], num[b+1] = num[b+1], num[b]
                        done = False
                if done:
                    return
                print(num)

        def main():
                                
            print("[Please Enter Numbers Separated by Comma]")
            nums = input("Enter numbers:\n").split(',')
            numsList = [int(n) for n in nums]


            bubbleSort(numsList)
            print("*"*35)
            print("Bubble Sorted Numbers: ")
            time.sleep(2)
            print(numsList)
            print("*"*35)

        main()

        Ask_Again = int(input("What you want to do? \n [1] Try Again \n [2] Go Back to Sorting System \n [3] Exit \n I choose: "))
        if Ask_Again == 1: pass
        elif Ask_Again == 2: Sorting()
        elif Ask_Again == 3:
            print("Thank you for patrionazing our program!")
            os._exit(0) 
        else:
            print ("Please choose properly from menu!")

def InsertionSort():
    while True:
        InsertionList = []
        Ask = int(input("Number of times that will you insert: "))
        for i in range(0,Ask):
            Number= int(input("Please enter a number: "))
            InsertionList.append(Number)
        Original_List = InsertionList.copy()
        lenght = range(1, len(InsertionList))
        print("Here is the your unsorted list: \n " + str(Original_List))
        Move =0
        for i in lenght:
            Elements_to_sort = InsertionList[i]
            while InsertionList[i-1]>Elements_to_sort and i>0:
                InsertionList[i], InsertionList[i-1] = InsertionList[i-1], InsertionList[i]
                i=i-1
                Move = Move+1
                print(InsertionList)
        time.sleep(3)
        print(" The total number of sorting happened: " + str(Move))
        time.sleep(2)
        print("Your sorted list: \n" + str(InsertionList))

        Ask_Again = int(input("What you want to do? \n [1] Try Again \n [2] Go Back to Sorting System \n [3] Exit \n I choose: "))
        if Ask_Again == 1: pass
        elif Ask_Again == 2: Sorting()
        elif Ask_Again == 3:
            print("Thank you for patrionazing our program!")
            os._exit(0) 
        else:
            print ("Please choose properly from menu!")

def MergeSort():
    while True:
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
                        print(num)

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
        Ask_Again = int(input("What you want to do? \n [1] Try Again \n [2] Go Back to Sorting System \n [3] Exit \n I choose: "))        
        if Ask_Again == 1: pass
        elif Ask_Again == 2: Sorting()
        elif Ask_Again == 3:
            print("Thank you for patrionazing our program!")
            os._exit(0) 
        else:
            print ("Please choose properly from menu!") 

def QuickSort():
    while True:
        def partition(quick_sort_list, lower_value, higher_value): 
                i = (lower_value-1)		 
                pivot = quick_sort_list[higher_value]	 

                for j in range(lower_value, higher_value): 
                        if quick_sort_list[j] <= pivot: 
                                i = i+1
                                quick_sort_list[i], quick_sort_list[j] = quick_sort_list[j], quick_sort_list[i] 

                quick_sort_list[i+1], quick_sort_list[higher_value] = quick_sort_list[higher_value], quick_sort_list[i+1] 
                return (i+1) 

        def quickSort(quick_sort_list, lower_value, higher_value): 
                if len(quick_sort_list) == 1: 
                        return quick_sort_list 
                if lower_value < higher_value: 
                        index_element = partition(quick_sort_list, lower_value, higher_value) 
                        quickSort(quick_sort_list, lower_value, index_element-1) 
                        quickSort(quick_sort_list, index_element+1, higher_value) 
        quick_sort_list = []
        Ask = int(input("Number of times that will you insert: "))
        for i in range(0,Ask):
            Number= int(input("Please enter a number: "))
            quick_sort_list.append(Number)
        n = len(quick_sort_list) 
        quickSort(quick_sort_list, 0, n-1) 
        print("Sorted array is:") 
        for i in range(n): 
                print("%d" % quick_sort_list[i])

        Ask_Again = int(input("What you want to do? \n [1] Try Again \n [2] Go Back to Sorting System \n [3] Exit \n I choose: "))        
        if Ask_Again == 1: pass
        elif Ask_Again == 2: Sorting()
        elif Ask_Again == 3:
            print("Thank you for patrionazing our program!")
            os._exit(0) 
        else:
            print ("Please choose properly from menu!") 

def SelectionSort():
    while True:
        selection_sort_list = []
        Ask = int(input("Number of times that will you insert: "))
        for i in range(0,Ask):
            Number= int(input("Please enter a number: "))
            selection_sort_list.append(Number)
        selection_sort_copy = selection_sort_list.copy()
        move = 0
        print("Here is the your unsorted list: \n " + str(selection_sort_copy))
        time.sleep(3)
        print("Here is the process of sorting your list: ")
        for elements in range(len(selection_sort_list)):
            lowest_index = elements
            time.sleep(2)
            print(selection_sort_list)
            move = move + 1
            for i in range(elements, len(selection_sort_list)):
                if selection_sort_list[i] < selection_sort_list[lowest_index]:
                    lowest_index = i
            (selection_sort_list[elements], selection_sort_list[lowest_index]) = (selection_sort_list[lowest_index],selection_sort_list[elements])    
        time.sleep(2)
        print("Your sorted list: \n" + str(selection_sort_list))
        
        Ask_Again = int(input("What you want to do? \n [1] Try Again \n [2] Go Back to Sorting System \n [3] Exit \n I choose: "))
        if Ask_Again == 1: pass
        elif Ask_Again == 2: Sorting()
        elif Ask_Again == 3: 
            print("Thank you for patrionazing our program!")
            os._exit(0) 
        else:
            print ("Please choose properly from menu!")      

def ShellSort():
    while True:
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
              print(numsList)
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
        Ask_Again = int(input("What you want to do? \n [1] Try Again \n [2] Go Back to Sorting System \n [3] Exit \n I choose: "))
        if Ask_Again == 1: pass
        elif Ask_Again == 2: Sorting()
        elif Ask_Again == 3:
            print("Thank you for patrionazing our program!")
            os._exit(0) 
        else:
            print ("Please choose properly from menu!")

def StackSystem():
    while True:
        time.sleep(1)
        print("Welcome to Stack System")
        StackMenu = int(input("Choose your process: \n [1] Add Car \n [2] Remove Car \n [3] Exit System \n I choose: "))
        if StackMenu == 1: AddCarStack()
        elif StackMenu == 2: RemoveCarStack()
        elif StackMenu == 3: 
            print("Thank you for patrionazing our program!")
            os._exit(0) 
        else:
            print ("Please choose between the given system")
 
def AddCarQueue():
    global ArrivalQueue
    global DepartalQueue
    print("Remaining park slot: " + str(10-len(CarGarageQueueSystem)))
    PlateNumberofCar = input("Please provide the platenumber of your car: ")
    CarGarageQueueSystem.append(PlateNumberofCar)
    time.sleep(3)
    print("Car Arriving: " + PlateNumberofCar)
    print(str(CarGarageQueueSystem))
    time.sleep(2)
    print("Remaining park slot: " + str(10-len(CarGarageQueueSystem)))
    ArrivalQueue +=1
    print("Number of arrivals happened: " + str(ArrivalQueue))
    print("Number of departals happened: " + str(DepartalQueue))

def RemoveCarQueue():
    global ArrivalQueue
    global DepartalQueue
    print("Here is the list of cars",  CarGarageQueueSystem)
    Remove = input("What car do you want to remove? ")
    IndexToBeRemove = int(CarGarageQueueSystem.index(Remove))
    if Remove in CarGarageQueueSystem:
        i = 0
        while i < IndexToBeRemove+1:
            print("Now Departing: " + str(CarGarageQueueSystem[i]))
            DepartalQueue += 1
            i+=1
            time.sleep(3)
        print("All cars will start to move back in the garage")
        time.sleep(5)
        CarGarageQueueSystem.remove(Remove)
        j=0
        while j!= IndexToBeRemove:
           print("Now Arriving: " + str(CarGarageQueueSystem[j]))
           ArrivalQueue +=1
           time.sleep(3)
        print("Number of arrivals happened: " + str(ArrivalQueue))
        print("Number of departals happened: " + str(DepartalQueue)) 

def QueueSystem():
    while True:
        time.sleep(1)
        print("Welcome to Queue System")
        StackMenu = int(input("Choose your process: \n [1] Add Car \n [2] Remove Car \n [3] Exit System \n I choose: "))
        if StackMenu == 1: AddCarQueue()
        elif StackMenu == 2: RemoveCarQueue()
        elif StackMenu == 3: 
            print("Thank you for patrionazing our program!")
            os._exit(0) 
        else:
            print ("Please choose between the given system")

def BinaryTree():
    while True:
                if __name__ == '__main__':
                    option = 0
                    root = None

                    while(option != 3):
                        print("")
                        printOption()
                        option = int(input("Enter your Choice: "))
                        

                        if (option == 1):
                            print("")
                            print("[Please Enter Numbers Separated by Comma]")
                            nums = input("Enter numbers:\n").split(',')
                            keys = [int(num) for num in nums]
                            
                    
                            for key in keys:
                                root = insert(root, key)
                            
                            print("*"*35)
                            inorder(root)
                            print("")
                            print("*"*35)

                        elif (option == 2):
                            print("[Please Enter the Number to be Deleted]")
                            numDel = int(input("Enter Number: "))
                            root = deleteNode(root, numDel)
                            print("*"*35)
                            inorder(root)
                            print("")
                            print("*"*35)

                        else:
                            print("[!]Please choose from options above.")
                

def CarPark():

    print("Welcome to Car Garage")
    System = int(input("Please choose your system: \n [1] Stack System \n [2] Queue System \n [3] Main Menu \n [4] Exit Program \n I choose system: "))
    if System == 1: StackSystem()
    elif System == 2: QueueSystem()
    elif System == 3: MainMenu()
    elif System == 4:
        print("Thank you for patrionazing our program!")
        os._exit(0) 
    else:
        print ("Please choose between the given system")

def Factorial():
    Factorial = []
    print("Hello, thank you for choosing Factorial!")
    AskNumber = int(input("Please input a number: "))
    FactorialSum = 1
    if AskNumber > 0:
        while True:
            for Number in range (1, AskNumber+1):
                Factorial.append(Number)
                FactorialSum = FactorialSum * Number
            Factorial.reverse()
            print("Here is the list of numbers in factorial number:")
            time.sleep(3)
            print(str(Factorial))
            print("Here is the factorial product:")
            time.sleep(3)
            print(FactorialSum)
            Next = int(input("What you want do? \n [1] Go to Main Menu \n [2] Try Again \n [3] Exit Program \n I choose: "))
            if Next == 1: 
                MainMenu()
                time.sleep(4)
            elif Next == 2:
                break
            elif Next == 3:
                print("Thank you for patrionazing our program!")
                os._exit(0) 
            else:
                print("Please try  again")
    else:
        print("It must be postive integer")

def Fibonacci():
    while True:
        FibonacciList = []
        print("Hello, thank you for choosing Fibonnaci!")
        AskNumber = int(input("Please input a number: "))
        FirstNumber = 0
        SecondNumber = 1
        Count = 2
        if AskNumber == 1:
            print("Here is your fibonacci number: ")
            time.sleep(1)
            print(FirstNumber)
        elif AskNumber > 1:
            print("Here is your fibonacci number: ")
            FibonacciList.append(0)
            FibonacciList.append(1)
            while Count < AskNumber:
                NextNumber = FirstNumber + SecondNumber
                FibonacciList.append(NextNumber)
                FirstNumber = SecondNumber
                SecondNumber = NextNumber
                Count  +=1
            time.sleep(3)
            print(str(FibonacciList))
        else:
            print("You must enter postive number =)")
        Ask_Again = int(input("What you want to do? \n [1] Try Again \n [2] Main Menu \n [3] Exit \n I choose: "))
        if Ask_Again == 1: pass
        elif Ask_Again == 2: MainMenu()
        elif Ask_Again == 3:
            print("Thank you for patrionazing our program!")
            os._exit(0) 
        else:
            print ("Please choose properly from menu!")

def Sorting():
    while True:
        time.sleep(1)
        print("Welcome to Sorting System")
        SortMenu = int(input("Choose your process: \n [1] Bubble Sort \n [2] Merge Sort \n [3] Shell Sort \n [4] Insertion Sort \n [5] Quick Sort \n [6] Selection Sort \n [7] Main Menu \n [8] Exit Program I choose: "))
        if SortMenu == 1: BubbleSort() #Done
        elif SortMenu == 2: MergeSort() #Done
        elif SortMenu == 3: ShellSort() #Done
        elif SortMenu == 4: InsertionSort() #Done
        elif SortMenu == 5: QuickSort()  #Done
        elif SortMenu == 6: SelectionSort() #Done
        elif SortMenu == 7: MainMenu()
        elif SortMenu == 8:
            print("Thank you for patrionazing our program!")
            os._exit(0) 
        else:
            print ("Please choose properly from menu!")

def TowerOfHanoi():

    def moveDisks(disks, inPos, toPos):
        print("\nHanoi disc {} moved from {} to {}.".format(disks, inPos,toPos))

    def runHanoi(disks, inPos, auxPos, toPos):
        global count
        if disks == 0:
            pass
        else:
            runHanoi(disks-1, inPos, toPos, auxPos)
            moveDisks(disks, inPos,toPos)
            #time.sleep(1)
            runHanoi(disks-1, auxPos, inPos, toPos)
            count += 1
    disks = int(input("Enter Number of Hanoi Disks: "))

    print("-="*18)
    print("  Hanoi Disks: Smallest at disk 1 ")
    print("    {} disks with columns A B C   ".format(disks))
    print("-="*18)
    runHanoi(disks, "A", "B", "C")
    print("\n-="*18)
    print("Moves Made: ", count)
    print("-="*18)
    HanoiAsk = int(input("What do you want to do? \n [1] Try Again \n [2] Main Menu \n [3] Exit \n I want: "))
    if HanoiAsk == 1: pass
    elif HanoiAsk == 2: MainMenu()
    elif HanoiAsk == 3:
        print("Thank you for patrionazing our program!")
        os._exit(0) 
    else:
        print("Goingback to MainMenu... you must follow the rule...")
        MainMenu()

def MainMenu():
    print(26*"-")
    print("Welcome to our program")
    print("Choose what you want \n [1] Binary Tree \n [2] Car Park \n [3] Factorial \n [4] Fibonacci \n [5] Linked List \n [6] Sorting \n [7] Tower of Hanoi \n [8] Exit Progam")
    MainMenuQuestion = int(input("What do you choose? "))
    while True:
        if MainMenuQuestion == 1:BinaryTree() #Done
        elif MainMenuQuestion == 2: CarPark() #Done
        elif MainMenuQuestion == 3: Factorial() #Done
        elif MainMenuQuestion == 4: Fibonacci() #Done
        elif MainMenuQuestion == 5: LinkedList() #Done
        elif MainMenuQuestion == 6: Sorting()
        elif MainMenuQuestion == 7: TowerOfHanoi() #Done
        elif MainMenuQuestion == 8: break 
        else: 
            print("Pleaase choose number from menu =)") 
            MainMenu()

MainMenu()
