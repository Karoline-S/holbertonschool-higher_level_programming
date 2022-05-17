#!/usr/bin/python3
"""creates a singly linked list"""


class Node:
    """
    class for Node
    """
    def __init__(self, data, next_node=None):
        """
        initialise an instance of Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        retrieves data for instance
        """
        return self.data

    @data.setter
    def data(self, value):
        """
        sets the value for data for an instance
        """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """
        retrieves next_node for instance
        """
        return next_node

    @next_node.setter
    def next_node(self, value):
        """
        sets the value for next_node for instance
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """
    class for a singly linked list
    """

    def __init__(self):
        self.__head = None


    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head:
            current = self.__head
            if current.data >= value:
                self.head = new_node
                new_node.next_node = current.next_node
            else:
                while (current.next_node and current.data < value):
                    previous = current
                    current = current.next_node
                if current.next_node:
                    previous.next_node = new_node
                    new_node.next_node = current
                else:
                    current.next_node = new_node
        else:
            self.__head = new_node


    def __str__(self):
        res = ""

        current = self.__head

        while current:
            res += str(current.data) + '\n'
            current = current.next_node

        return res
