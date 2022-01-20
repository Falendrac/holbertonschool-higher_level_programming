#!/usr/bin/python3
"""
100-singly_linked_list

    Module that defines a class Node and a class Singly linked list
"""


class Node:
    """
    Node - Define a node of a singly linked list

    ...

    Attributes
    ----------

    __data : int
        define the data of a node of linked list

    __next_node : Node
        define the next node of a linked list

    Methods
    -------

    data(self)
        the getter of data attribute

    data(self, value)
        the setter of data attribute

    next_node(self)
        the getter of next_node attribute

    next_node(self, value)
        the setter of data attribute
    """

    data = 0
    next_node = None

    def __init__(self, data, next_node=None):
        """
        init - Instanciation for data and next_node

        ...

        Parameters
        ----------
        data : int
            the data that define the node
        next_node : None
            the next_node of linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        data - The getter for data
        """
        return self.__data

    @data.setter
    def data(self, data):
        """
        data - The setter for data check if is valid

        ...

        Parameters
        ----------
        data : int
            the data we want to set in node

        Raises
        ------
        TypeError
            if data is not an integer
        """
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        next_node - This is the getter of next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        next_node - The setter of next_node

        ...

        Parameters
        ----------
        value : node
            the node we want to set

        Raise
        -----
        TypeError
            if value is not None
        """
        if isinstance(value, Node) or not value:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    Node - Define a node of a singly linked list

    ...

    Attributes
    ----------

    __head : node


    Methods
    -------

    sorted_insert(self, value)
        insert a new node in the linked list by sort
    """

    def __init__(self):
        """
        init - Instanciation for linked_list

        ...

        Parameters
        ----------
        head : None
            the head of the linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        sorted_insert - Insert a new node with value by sorted

        ...

        Parameters
        ----------
        value : int
            the value of the new node
        """
        newnode = Node(value)
        if self.__head:
            if self.__head.data > value:
                newnode.next_node = self.__head
                self.__head = newnode
            else:
                current = self.__head
                while(current.next_node and current.next_node.data < value):
                    current = current.next_node
                newnode.next_node = current.next_node
                current.next_node = newnode
        else:
            self.__head = newnode

    def __str__(self):
        """
        str - Convert the values of linked list in str

        Print all value
        """
        current = self.__head
        if not current:
            return ("")
        while current and current.next_node:
            print("{}".format(current.data))
            current = current.next_node
        return str(current.data)
