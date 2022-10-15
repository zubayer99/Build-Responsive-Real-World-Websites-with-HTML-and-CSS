class LinkedList:
  def __init__(self, a):
        if type(a) == list:
            self.head = Node(a[0],None) 
            tail = self.head
            
            for i in range(1, len(a)) :
                temp = Node(a[i],None) 
                tail.next = temp
                tail = tail.next 
        else :
            self.head = a
            
  def countNode(self) :
        count = 0 
        head = self.head
        while head != None :
            count += 1 
            head = head.next
            
        return count
    
  def printList(self) :
        head = self.head 
        store = ''
        
        while head != None: 
            if head.next != None:
                store += str(head.element) + ', ' 
            else:
                store += str(head.element) 
            head = head.next
        print(store)

  def nodeAt(self,idx):
    head = self.head 
    flag = False 
    ans = None 
    count = 0
    
    while head != None:
        if count == idx:
            flag = True 
            ans = head
            break 
        else:
            ans = 'Invalid index' 
        count += 1 
        head = head.next
        
        return ans
    
  def get(self, idx):
    head = self.head 
    flag = False 
    ans = None 
    count = 0
    while head != None:
        if count == idx:
            flag = True 
            ans = head.element
            break 
        elif count <0 or count > idx:
            flag = False 
        count += 1 
        head = head.next
        
    if flag == True :
        return ans 
    else :
        return None
  
  def set(self,idx, elem):
    head = self.head 
    flag = False 
    ans = None 
    new_ans = None 
    count = 0
    
    while head != None:
        if count == idx:
            flag = True 
            ans = head.element 
            new_ans = elem 
            head.element = new_ans
            break 
        count += 1 
        head = head.next
        
    if flag == True:
        return ans 
    else:
        return None
    
  def indexOf(self,elem):
        head = self.head 
        flag = False 
        ans = None 
        count = 0
        
        while head != None:
            if head.element == elem :
                flag = True
                ans = count 
            count += 1 
            head = head.next
            
        if flag == True:
            return ans 
        else:
            return -1
        
  def contains(self, elem):
    head = self.head
    
    while head != None:
        if head.element == elem:
            ans = True 
        else:
            ans = False 
            head = head.next
    return ans

  def copyList(self):
        head = self.head 
        count = 0 
        copyHead = None 
        copyTail = None
        while head != None: 
            if copyHead == None :
                copyHead = Node (head.element, head.next)
                copyTail = copyHead 
            else :
                temp2 = Node (head.element, head.next) 
                copyTail.next = temp2
                copyTail = copyTail.next 
            head = head.next
        return copyHead

  def reverseList(self):
    copyHead = None 
    head = self.head 
    nextNode = None 
    while head != None:
        nextNode = head.next 
        head.next = copyHead 
        copyHead = head
        head = nextNode 
    return copyHead
  
 
  def insert(self, elem, idx):
    newlode = Node(elem, None)
        
     if idx == 0:
       newNode.next = self.head
       self.head = newNode 
     else:
       pred = self.nodeAt(idx-1) 
       newNode. next = pred.next 
       pred.next = newNode
            
  def remove(self, idx):
    removed = (self.nodeAt(idx)).element 
    removeNode = self.nodeAt(idx)
    
    if idx == 0:
        self.head = self.head.next 
    else:
        pred = self.nodeAt(idx-1)
        pred.next = removeNode.next 
    removeNode.next = None 
    removeNode.element = None 
    removeNode = None
    
    return removed

  def rotateLeft(self):
    check = self.head 
    self.head = self.head.next 
    head = self.head 
    tail = None
        
    while head != None:
        tail = head
        head = head.next 
    tail.next = check 
    check.next = None 
    return check
  
  def rotateRight(self):
    head = self.head 
    tail = self.nodeAt((self.countNode())-1) 
    prev = self.nodeAt((self.countNode())-2) 
    check = None
    
    while head != None: 
        if self.nodeAt() == head:
            check = head 
            prev.next = None
            head = head.next 
    self.head = tail 
    tail.next = check 
    return self.head