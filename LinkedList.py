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


def main():
    node = LinkedList.generate(node_range=10)

    print("Node 1 is: ", node[1])

    for i in range(len(node)):
        LinkedList.traverse(node[i])


if __name__ == "__main__":
    main()

