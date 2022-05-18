#!/usr/bin/python3
"""create a singly linked list"""


class Node:
    """
    define a class Node
    initialise each instance with arg data and optional arg next_node
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """
    class to create a singly linked list
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head

        while current.next_node is not None:
            if current.next_node.data >= new_node.data:
                break
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        res = ""

        current = self.__head

        while current is not None:
            res += str(current.data)
            if current.next_node is not None:
                res += "\n"
            current = current.next_node

        return res
