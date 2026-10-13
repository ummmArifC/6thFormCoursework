#-------Node----------#
class Node():
#--------constructor--------#
 def __init__(self,data):
    self.data = data
    self.next = None

 def getData(self):
   return self.data
 
 def getNext(self):
   return self.next

 def setNext(self, newNext):
   self.next = newNext 
   
#--------Linked List---------#

class LinkedList():
#--------constructor-------#
 def __init__(self):
   self.head = None

 def traverse(self):
  if self.head == None:
    print("List Empty")
    return
  
  current = self.head
  while current != None:
    print(current.getData())
    current = current.getNext()

 def traverse_v2(self):
    current = self.head

    if current == None:
        print("List Empty")
    else:
        while current != None:
            print(current.getData())
            current = current.getNext()

# -------instantiate object------#


############# MAIN PROGRAM ###################
myList = LinkedList()  

myList.traverse()