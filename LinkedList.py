import numpy as np

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def generate(self, node_range):
        for _ in range(node_range):
            new_val = round(np.random.rand(), 3)  # prepend for O(1) efficiency
            self.insert_at_head(new_val)  # insert at head

    def insert_at_head(self, value):
        new_node = Node(value)  # create new node
        new_node.next = self.head  # point new node to current head
        self.head = new_node  # update head to new node

    def insert(self, value, position):
        """
        Inserts a value at a specific index
        0-based indexing is used.
        """
        new_node = Node(value)  # create new node
        
        if position <= 0 or not self.head:  # insert at head if position is 0 or list is empty
            self.insert_at_head(value)
            return

        current = self.head  # start from head
        count = 0  # position counter

        while current.next and count < position - 1:  # Traverse to the node just before the insertion point
            current = current.next  # move to next node
            count += 1  # increment position counter
        
        new_node.next = current.next  # point new node to the next node
        current.next = new_node  # link current node to new node

    def delete_by_value(self, target_value):
        """
        Deletes the first node found with the matching value.
        """
        if not self.head:  # empty list
            return

        if self.head.data == target_value:  # if head needs to be deleted
            self.head = self.head.next  # update head to next node
            return

        current = self.head  # start from head
        while current.next:  # traverse the list
            if current.next.data == target_value:  # find the target value
                current.next = current.next.next  # bypass the node to delete
                return
            current = current.next  # move to next node

    def find_lowest(self):
        """
        Returns the minimum value in the list
        """
        if not self.head:  # empty list
            return None
        
        lowest = self.head.data  # initialize lowest with head data
        current = self.head.next  # start from second node
        while current:  # traverse the list
            if current.data < lowest:  # check for lowest value
                lowest = current.data  # update lowest
            current = current.next  # move to next node
        return lowest

    def traverse(self):
        """
        Prints the list visually
        """
        current = self.head  # start from head
        while current:  # traverse the list
            print(current.data, end=" => ")  # print current node data
            current = current.next  # move to next node
        print("None")

    def __len__(self):
        """
        Allows use of len(linked_list_instance)
        """
        count = 0  # initialize count
        current = self.head  # start from head
        while current:  # traverse the list
            count += 1  # increment count
            current = current.next  # move to next node
        return count


class DoubleLinkedList:
    def __init__(self, value):
        self.data = value
        self.next = None  # pointer to next node
        self.prev = None  # pointer to previous node

    @staticmethod
    def generate(node_range):
        node = []  # list to hold nodes
        for i in range(node_range):
            node.append(DoubleLinkedList(round(np.random.rand(), 3)))
            if i > 0:
                node[i-1].next = node[i]  # link previous node to next node
                node[i].prev = node[i-1]  # link next node to previous node
        return node

    @staticmethod
    def traverse(head):
        currentNode = head  # start from head
        while currentNode:  # traverse the list
            print(currentNode.data, end= " <=> ")  # print current node data
            currentNode = currentNode.next  # move to next node
        print("Null")
    
    @staticmethod
    def reverse_traverse(tail):  # traverse from tail to head
        currentNode = tail  # start from tail
        while currentNode:  # traverse the list
            print(currentNode.data, end= " <=> ")  # print current node data
            currentNode = currentNode.prev  # move to previous node
        print("Null")

    @staticmethod
    def find_lowest(head):
        currentNode = head  # start from head
        lowest = head.data  # initialize lowest with head data
        while currentNode:  # traverse the list
            if currentNode.data < lowest:  # check for lowest value
                lowest = currentNode.data  # update lowest
            currentNode = currentNode.next  # move to next node
        return lowest
    
    @staticmethod
    def delete_node(head, node_to_delete):
        if head == node_to_delete:  # if head is the node to delete
            return head.next  # return new head

        currentNode = head  # start from head
        while currentNode:  # traverse the list
            if currentNode == node_to_delete:  # find the node to delete
                if currentNode.prev:  # link previous node to next node
                    currentNode.prev.next = currentNode.next  # bypass the node to delete
                if currentNode.next:  # link next node to previous node
                    currentNode.next.prev = currentNode.prev  # bypass the node to delete
                return head
            currentNode = currentNode.next  # move to next node
        
        return head
    
    @staticmethod
    def insert_node(head, new_node, position):
        if position == 0:
            new_node.next = head
            if head:
                head.prev = new_node
            return new_node
        
        currentNode = head
        currentPosition = 0
        
        while currentNode and currentPosition < position - 1:
            currentNode = currentNode.next
            currentPosition += 1
        
        if currentNode is None:
            return head
        
        new_node.next = currentNode.next
        new_node.prev = currentNode
        if currentNode.next:
            currentNode.next.prev = new_node
        currentNode.next = new_node
        
        return head

    @staticmethod
    def length(head):
        currentNode = head
        count = 0
        while currentNode:
            count += 1
            currentNode = currentNode.next
        return count


class CircularLinkedList:
    def __init__(self, value):
        self.data = value
        self.next = None

    @staticmethod
    def generate(node_range):
        node = []
        for i in range(node_range):
            node.append(CircularLinkedList(round(np.random.rand(), 3)))
            if i > 0:
                node[i-1].next = node[i]
        node[-1].next = node[0]  # Making it circular
        return node

    @staticmethod
    def traverse(head, limit=20):
        currentNode = head
        count = 0
        while currentNode and count < limit:
            print(currentNode.data, end= " => ")
            currentNode = currentNode.next
            count += 1
        print("... (circular)")

    @staticmethod
    def find_lowest(head, limit=20):
        currentNode = head
        lowest = head.data
        count = 0
        while currentNode and count < limit:
            if currentNode.data < lowest:
                lowest = currentNode.data
            currentNode = currentNode.next
            count += 1
        return lowest

    @staticmethod
    def delete_node(head, node_to_delete, limit=20):
        if head == node_to_delete:
            return head.next
        
        currentNode = head
        count = 0
        while currentNode and count < limit:
            if currentNode.next == node_to_delete:
                currentNode.next = node_to_delete.next
                return head
            currentNode = currentNode.next
            count += 1
        
        return head

    @staticmethod
    def insert_node(head, new_node, position, limit=20):
        if position == 0:
            new_node.next = head
            return new_node
        
        currentNode = head
        currentPosition = 0
        count = 0
        
        while currentNode and currentPosition < position - 1 and count < limit:
            currentNode = currentNode.next
            currentPosition += 1
            count += 1
        
        if currentNode is None:
            return head
        
        new_node.next = currentNode.next
        currentNode.next = new_node
        
        return head
    
    @staticmethod
    def length(head, limit=20):
        currentNode = head
        count = 0
        while currentNode and count < limit:
            count += 1
            currentNode = currentNode.next
        return count

class OpsLinkedList:
    @staticmethod
    def linked_list_ops():
        linked_list = LinkedList()
        linked_list.generate(10)

        # Traverse
        print("Initial Linked List:")
        linked_list.traverse()

        # Lowest
        lowest_value = linked_list.find_lowest()  # Find lowest value
        print(f"Lowest value in the linked list is: {lowest_value}")

        # Delete
        val_to_delete = lowest_value  # Delete the node with the lowest value
        print(f"Deleting node with value: {val_to_delete}")
        linked_list.delete_by_value(val_to_delete)
        linked_list.traverse()

        # Insert
        new_val = round(np.random.rand(), 3)  # Insert a new random value
        print(f"Inserting {new_val} at position 5")
        linked_list.insert(new_val, 5)
        linked_list.traverse()

        # Length
        print(f"Length of the linked list is: {len(linked_list)}")

    @staticmethod
    def double_linked_list_ops():
        # Generate DoubleLinkedList
        node = DoubleLinkedList.generate(node_range=10)

        print("Node 1 is: ", node[1])

        # Traverse DoubleLinkedList
        for i in range(len(node)):
            DoubleLinkedList.traverse(node[i])

        # Find lowest value in DoubleLinkedList
        lowest_value = DoubleLinkedList.find_lowest(node[0])
        print("Lowest value in the double linked list is:", lowest_value)

        # Delete a node from DoubleLinkedList
        node_to_delete = node[3]
        print("Deleting node with value:", node_to_delete.data)
        head_after_deletion = DoubleLinkedList.delete_node(node[0], node_to_delete)
        DoubleLinkedList.traverse(head_after_deletion)

        # Insert a new node into DoubleLinkedList
        new_node = DoubleLinkedList(round(np.random.rand(), 3))
        head_after_insertion = DoubleLinkedList.insert_node(node[0], new_node, 5)
        DoubleLinkedList.traverse(head_after_insertion)

        # Calculate length of DoubleLinkedList
        length_of_list = DoubleLinkedList.length(node[0])
        print("Length of the double linked list is:", length_of_list)

    @staticmethod
    def circular_linked_list_ops():
        # Generate CircularLinkedList
        node = CircularLinkedList.generate(node_range=10)

        print("Node 1 is: ", node[1])

        # Traverse CircularLinkedList
        for i in range(len(node)):
            CircularLinkedList.traverse(node[i])

        # Find lowest value in CircularLinkedList
        lowest_value = CircularLinkedList.find_lowest(node[0])
        print("Lowest value in the circular linked list is:", lowest_value)

        # Delete a node from CircularLinkedList
        node_to_delete = node[3]
        print("Deleting node with value:", node_to_delete.data)
        head_after_deletion = CircularLinkedList.delete_node(node[0], node_to_delete)
        CircularLinkedList.traverse(head_after_deletion)

        # Insert a new node into CircularLinkedList
        new_node = CircularLinkedList(round(np.random.rand(), 3))
        head_after_insertion = CircularLinkedList.insert_node(node[0], new_node, 5)
        CircularLinkedList.traverse(head_after_insertion)

        # Calculate length of CircularLinkedList
        length_of_list = CircularLinkedList.length(node[0])
        print("Length of the circular linked list is:", length_of_list)

if __name__ == "__main__":
    OpsLinkedList.linked_list_ops()
    # OpsLinkedList.double_linked_list_ops()
    # OpsLinkedList.circular_linked_list_ops()

