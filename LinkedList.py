import numpy as np

class LinkedList:
    def __init__(self, value):
        self.data = value
        self.next = None

    @staticmethod
    def generate(node_range):
        node = []
        for i in range(node_range):
            node.append(LinkedList(round(np.random.rand(), 3)))
            if i > 0:
                node[i-1].next = node[i]
        return node

    @staticmethod
    def traverse(head):
        currentNode = head
        while currentNode:
            print(currentNode.data, end= " => ")
            currentNode = currentNode.next
        print("Null")
    
    @staticmethod
    def find_lowest(head):
        currentNode = head
        lowest = head.data
        while currentNode:
            if currentNode.data < lowest:
                lowest = currentNode.data
            currentNode = currentNode.next
        return lowest

    @staticmethod
    def delete_node(head, node_to_delete):
        if head == node_to_delete:
            return head.next
        
        currentNode = head
        while currentNode:
            if currentNode.next == node_to_delete:
                currentNode.next = node_to_delete.next
                return head
            currentNode = currentNode.next
        
        return head
    
    @staticmethod
    def insert_node(head, new_node, position):
        if position == 0:
            new_node.next = head
            return new_node
        
        currentNode = head
        currentPosition = 0
        
        while currentNode and currentPosition < position - 1:
            currentNode = currentNode.next
            currentPosition += 1
        
        if currentNode is None:
            return head
        
        new_node.next = currentNode.next
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

class DoubleLinkedList:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

    @staticmethod
    def generate(node_range):
        node = []
        for i in range(node_range):
            node.append(DoubleLinkedList(round(np.random.rand(), 3)))
            if i > 0:
                node[i-1].next = node[i]
                node[i].prev = node[i-1]
        return node

    @staticmethod
    def traverse(head):
        currentNode = head
        while currentNode:
            print(currentNode.data, end= " <=> ")
            currentNode = currentNode.next
        print("Null")

    @staticmethod
    def find_lowest(head):
        currentNode = head
        lowest = head.data
        while currentNode:
            if currentNode.data < lowest:
                lowest = currentNode.data
            currentNode = currentNode.next
        return lowest
    
    @staticmethod
    def delete_node(head, node_to_delete):
        if head == node_to_delete:
            return head.next
        
        currentNode = head
        while currentNode:
            if currentNode == node_to_delete:
                if currentNode.prev:
                    currentNode.prev.next = currentNode.next
                if currentNode.next:
                    currentNode.next.prev = currentNode.prev
                return head
            currentNode = currentNode.next
        
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
    def linked_list_ops():
        # Generate LinkedList
        node = LinkedList.generate(node_range=10)

        print("Node 1 is: ", node[1])

        # Traverse LinkedList
        for i in range(len(node)):
            LinkedList.traverse(node[i])

        # Find lowest value in LinkedList
        lowest_value = LinkedList.find_lowest(node[0])
        print("Lowest value in the linked list is:", lowest_value)

        # Delete a node from LinkedList
        node_to_delete = node[3]
        print("Deleting node with value:", node_to_delete.data)
        head_after_deletion = LinkedList.delete_node(node[0], node_to_delete)
        LinkedList.traverse(head_after_deletion)

        # Insert a new node into LinkedList
        new_node = LinkedList(0.123)
        head_after_insertion = LinkedList.insert_node(node[0], new_node, 5)
        LinkedList.traverse(head_after_insertion)

        # Calculate length of LinkedList
        length_of_list = LinkedList.length(node[0])
        print("Length of the linked list is:", length_of_list)


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
        new_node = DoubleLinkedList(0.456)
        head_after_insertion = DoubleLinkedList.insert_node(node[0], new_node, 5)
        DoubleLinkedList.traverse(head_after_insertion)

        # Calculate length of DoubleLinkedList
        length_of_list = DoubleLinkedList.length(node[0])
        print("Length of the double linked list is:", length_of_list)


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
        new_node = CircularLinkedList(0.789)
        head_after_insertion = CircularLinkedList.insert_node(node[0], new_node, 5)
        CircularLinkedList.traverse(head_after_insertion)

        # Calculate length of CircularLinkedList
        length_of_list = CircularLinkedList.length(node[0])
        print("Length of the circular linked list is:", length_of_list)

if __name__ == "__main__":
    # OpsLinkedList.linked_list_ops()
    # OpsLinkedList.double_linked_list_ops()
    OpsLinkedList.circular_linked_list_ops()

