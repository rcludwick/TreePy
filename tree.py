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
    def from_nested_lists(nested_list):
        '''
        Process children in a nested list or a combination thereof.
        '''
        return Tree(children=nested_list)

    @staticmethod
    def from_nested_dicts(nested_dict, add_root_node=True, root_value=None):
        '''
        Process children in an nested set of dictionaries

        @add_root_node should be true if there is more than
            one top level key in the dictionary, otherwise
            it can be false.

        '''
        pass

    @staticmethod
    def from_nested_doublets(nested_doublets):
        '''
        Process children as a nested list of doublets in
        (key, value) form

        ( ("a", "b"), ("c", ("d", "e")) )
        '''
        pass

    #-------------------------------------
    # ComparisonMethods
    #-------------------------------------

    @staticmethod
    def diff_trees(new, old):
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

        equal_values = self.value == other.value
        equal_lengths = len(self) == len(other)

        equal_nodes = equal_values and equal_lengths

        equal = equal_nodes
        if equal:

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

        The nodes that non list types will have value but no children.

        The nodes that are list types will have children but with value set to None.

        '''

        super(Tree, self).__init__()
        self.__value = value
        self.__children = []

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

    def append(self, item):
        try:
            assert isinstance(item, Tree)
            return self.__children.append(item)
        except AssertionError:
            #XXX:
            #Check to see if item is a list or tuple:
            #Otherwise ... create a Tree 
            pass

    #-------------------------------------
    #Special tree specific idioms
    #-------------------------------------

    def flat_value_iter(self, skip_none=True, deepest_first=False):
        '''
        A generator that yields the tree's values

        @skip_none will skip anything equal to None
        @deepest_first will yield deepest first
        '''
        if not deepest_first:
            if not skip_none or self.__value is not None:
                    yield self.__value

        for child in self.__children:
            for child_iter in child.flat_value_iter(skip_none=skip_none, 
                                           deepest_first=deepest_first):

                if not skip_none or child_iter is not None:
                    yield child_iter

        if deepest_first:
            if not skip_none or self.__value is not None:
                    yield self.__value

        raise StopIteration()


    def flat_node_iter(self, deepest_first=False):
        '''
        Yields the nodes of the tree themselves in a flat way.

        Use leaf.value to get the value of the node.
        '''

        if not deepest_first:
            yield self

        for child in self.__children:
            for child_iter in child.flat_node_iter(
                        deepest_first=deepest_first):

                yield child_iter

        if deepest_first:
            yield self

        raise StopIteration()


    def leaf_node_iter(self):
        '''
        A generator that iterates over the leaves.

        use leaf.value to access the value of the nodes of the tree
        '''
        for child in self._children:
            yield child
        raise StopIteration()

