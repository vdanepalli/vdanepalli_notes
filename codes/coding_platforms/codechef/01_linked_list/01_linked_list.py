class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class SinglyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    
    def insert_at_beginning(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
            return
        
        new_node.next = self.head
        new_node.prev = self.tail
        self.head = new_node
        self.tail.prev = self.head
        
    def insert_at_end(self, value):
        
        new_node = Node(value)
        
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
            return
        
        new_node.prev = self.tail
        new_node.next = self.tail.next
        self.tail = new_node
        
        
    def insert_at_index(self, index, value):
        new_node = Node(value)
        
        
        
    def get_head_value(self):
        if self.head is None:
            return -1 
        
        return self.head.value
    
    def get_tail_value(self):
        if self.tail is None:
            return -1
    
        return self.tail.value
    
    def find_node(self, value):
        if self.head is None:
            return False
        
        current = self.head
        
        while(current):
            if current.value == value:
                return True
            current = current.next
            
            if current == self.head:
                break
        
        return False
    
    def print_values(self):
        current = self.head
        while current is not None:
            print(current.value, end = ' ')
            current = current.next
            if current == self.head:
                break
        print() 
        
        
    def delete_at_index(self, index):
        pass
    
    
def singly_linked_list():
    sll = SinglyLinkedList()
    sll_data = [1, 2, 3, 9, 12, 39]
    
    for i in sll_data:
        if i < 10:
            print(f"Inserting {i} at end : ", end=' ')
            sll.insert_at_end(i)
            
        else:
            print(f"Inserting {i} at beginning : ", end=' ')
            sll.insert_at_beginning(i)
        sll.print_values()
            
    print(f"45 in sll? {sll.find_node(45)}")
    
    
singly_linked_list()
            
        
        