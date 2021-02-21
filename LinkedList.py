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

		

def main (): 
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
			
			elif (option == 4):
    				break
			else:
				print("[!]Please choose from options above.")
			

main()
print("K bye")