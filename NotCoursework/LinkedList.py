#<-----------LINKED LIST CLASS----------->#

class LinkedList():
    # constructor
    def __init__(self, headData):
        self.head = Node(headData)

    def getHead(self):
        return self.head
    
    def getData(self):
        return self.data
    
    def add(self, newData):
        return None
    
    def traverseList(self):

        # start at the head/start pointer
        current = self.head # memory refernece to the first item

        # check if list is empty
        if current == None:
            print("List is empty")         
        else:
            print(current.getData()) # output item
            
            while current.getNext() != None:  # repeat until we get to the end 
                current = current.getNext() # reset current to next item
                print(current.getData()) # output the data

        # output item 

#<------------------ADDING NEW NODE-------------------->#



#<--------------------NODE CLASS---------------------->#
class Node():
    # constructor
    def __init__(self,newData):
        self.data = newData
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setNext(self, newNext):
        self.next = newNext


#<-----------------NODE RECORD--------------->#

# initialise to none as the linked list is empty

head = None         

############################################
#<--------------MAIN PROGRAM-------------->#
############################################

# create a variable to hold the name of first person to put in list
firstPerson = input("What is the first person in your list?: ")

# instantiated a linked list with first person setup
myList = LinkedList(firstPerson)

# for testing purposes of traversal
#newNode = Node("tony")
#myList.getHead().setNext(newNode)

#myList.traverseList()