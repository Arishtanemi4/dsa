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


def main():
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

if __name__ == "__main__":
    main()

