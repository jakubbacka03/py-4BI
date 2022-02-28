class LinkedList:
    def __init__(self):
        self.length = 0
        self.headNode = None
        self.tail = None

    def addNode(self, value):
        pass

    def getValues(self, index):
        if index < 0 or index >= self.length:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.value

    def getHead(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

        self.length += 1

    def getTail(self, value):
        curr = self.head
        if curr is None:
            self.head = Node(value)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(value)

        self.length += 1

    def removeValues(self, value):
        pass

    def insert(self, value, position):
        if position <= 0:
            self.add(value)

        elif position > (self.length() - 1):
            self.append(value)
        else:
            node = Node(value)
            pre = self.__head
            count = 0

            while count < (position - 1):
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return  self.value

    def setNextNode(self, node):
        self.next = node