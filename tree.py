#!/usr/bin/env python

from collections import OrderedDict
import types
import itertools

class Error(Exception):
    pass

class Tree(object):
    '''
    The Tree class builds a tree from an ordered dict or a series of tuples.
    Each subnode is of type Tree
    '''

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

        equal = self.value == other.value

        for my_child, other_child in itertools.izip(self, other):
            equal = my_child == other_child
            if not equal:
                break

        return equal


    #-------------------------------------
    # Init and properties
    #-------------------------------------

    def __init__(self, value, children=None):
        '''
        Init method.

        @value:  value for the node to hold.
        @children:  new value for the children.
        '''

        super(Node, self).__init__()
        self.__value = value
        self.__children = []

        if isinstance(children, types.ListType) \
                    or isinstance(children, types.TupleType) \
                    or isinstance(children, Tree):

            self.__process_children_in_list(children)
        elif isinstance(children, types.OrderedDict):
            self.__process_children_in_ordered_dict(children)

    @property
    def value(self):
        return __value

    @value.setter
    def value(self, val):
        self.__value = val

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
        return Tree(value=self.__value, children=self._d.__getslice__(i,j))
        
    def next(self):
        return self.__children.next()
    
    def append(self, item):
        try:
            assert isinstance(item, Tree)
            return self.__children.append(item)
        except AssertionError:
            if isinstance(item,  
            
        return self.__children.append(item)

    #-------------------------------------
    #Special processing for incoming trees
    #-------------------------------------

    def __process_children_in_list(self, children):
        '''
        Process children in a list of lists or tuple of tuples or a combination thereof.
        '''
        try:
            for childpair in children:
                if isinstance(childpair, types.ListType) or isinstance(child, types.TupleType):
                    if len(childpair) == 2:
                        child, grandchildren = childpair
                        treenode = Tree(value=child, children=grandchildren)
                        self.__children.append(treenode)
                    if len(childpair) = 1:
                        child = childpair
                        treenode = Tree(value=child)
                        self.__children.append(treenode)

                elif isinstance(childpair, OrderedDictionary):
                    self.__process_children_in_ordered_dict(childpair)

        except AttributeError, AssertionError:
            raise Error('Type is not iterable')

    def __process_children_in_ordered_dict(self, children):
        '''
        Process children as an ordered dict.
        '''
        try:
            assert(isinstance(children, OrderedDict))
            for child, grandchildren in child.iteritems():
                treenode = Tree(value=child, children=grandchildren)
                self.__children.append(treenode)

        except AssertionError:
            raise Error("Not an ordered dictionary")
