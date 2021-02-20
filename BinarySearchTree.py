
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
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

 
if __name__ == '__main__':
    option = 0
    while(option != 3):
        print("")
        printOption()
        option = int(input("Enter your Choice: "))
        

        if (option == 1):
            print("")
            print("[Please Enter Numbers Separated by Comma]")
            nums = input("Enter numbers:\n").split(',')
            keys = [int(num) for num in nums]
            
            root = None
    
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

print("K. Bye")