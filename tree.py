#!/usr/bin/env python

import types
import itertools
import collections

class Error(Exception):
    pass

class Tree(object):
    '''
    The Tree class builds a tree from a series of tuples or iteraable.
    Each subnode is of type Tree.
    '''
    #-------------------------------------
    # Tree Boolean Tests
    #-------------------------------------

    @staticmethod
    def is_iterable(thing):
        iterable = isinstance(thing, collections.Iterable)
        string = isinstance(thing, types.StringTypes)
        return iterable and not string

    #-------------------------------------
    # Tree Factory Methods
    #-------------------------------------

    @staticmethod
    def from_nested_singlets(ordered_list):
        '''
        Process children in a list of lists or tuple of tuples 
        or a combination thereof.
        '''
        pass

    #-------------------------------------
    # Loop check
    #-------------------------------------
    def has_loop(self):
        '''
        returns True if tree has a loop where nodes in a tree reference
        nodes above the tree
        '''
        return self.__loop_check()

    def __loop_check(self, visited=None):
        '''
        Implements a loop check function
        '''
        visited = visited if visited is not None else []

        for child in self.__children:
            if child in visited:
                return True

            visited.append(child)
            child_has_loop = child.__loop_check(visited=visited)

            if child_has_loop:
                return True

            visited.pop()
        return False

    #-------------------------------------
    # Tree Compare functions
    #-------------------------------------

    def __eq__(self, other):
        '''
        Performs a deep compare.
        '''
        if not isinstance(other, Tree):
            return False

        if self.has_loop() || other.has_loop():
            raise Error("Cannot compare trees.  Loop detected.")

        equal_values = self.value == other.value 
        equal_lengths = len(self) == len(other)

        equal_nodes = equal_values and equal_lengths

        equal = equal_nodes
        if equal_nodes:

            for my_child, other_child in itertools.izip(self, other):

                equal = my_child == other_child

                if not equal:
                    break

        return equal


    #-------------------------------------
    # Init and properties
    #-------------------------------------

    def __init__(self, value=None, children=None):
        '''
        Init method.

        @value:  value for the node to hold.
        @children:  new value for the children.

        The children should accept nested lists or tuples in the style:

        [ 'a', 'b', ['c', 'd'] , ['e'], ['f', 'g', ['h', ['i', ['j']]]]]

        '''

        super(Tree, self).__init__()
        self.__value = value
        self.__children = []

        if isinstance(children, types.StringTypes):
            raise Error("String passed into children parameter")

        is_iterable = Tree.is_iterable(children)
        if is_iterable:

            for child in children:

                is_tree_node = isinstance(child, Tree)
                is_parent = Tree.is_iterable(child)

                if is_tree_node:
                    self.__children.append(child)

                elif is_parent:
                    parent = Tree(value=None, children=child)
                    self.__children.append(parent)

                else:
                    leaf = Tree(value = child)
                    self.__children.append(leaf)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    @property
    def children(self):
        return self.__children


    #-------------------------------------
    #List Operations
    #-------------------------------------

    def __len__(self):
        return len(self.__children)

    def __iter__(self):
        return iter(self.__children)

    def __reversed__(self):
        return self.__children.__reversed__()

    def __contains__(self, item):
        return item in self.__children

    def __getitem__(self, index):
        try:
            return self.__children[index]
        except IndexError:
            raise IndexError('Index out of range.')

    def __setitem__(self,key,value):
        try:
            return self.__children.__setitem__(key,value)
        except IndexError:
            raise IndexError('List assignment index out of range.')

    def __getslice__(self, i, j):
        return Tree(value=self.__value, children=self.__children.__getslice__(i,j))

    def next(self):
        return self.__children.next()

    def append(self, item):
        try:
            assert isinstance(item, Tree)
            return self.__children.append(item)
        except AssertionError:
            #XXX:
            #Check to see if item is a list or tuple:
            #Otherwise ... create a Tree 
            pass

        return self.__children.append(item)

    #-------------------------------------
    #Special tree specific idioms
    #-------------------------------------

    def flatten_iter(self):
        pass

    def flatten(self):
        pass

    def leaf_iter(self):
        pass

    def flatten_leafs(self):
        pass

    #-------------------------------------
    #Special processing for incoming trees
    #-------------------------------------


