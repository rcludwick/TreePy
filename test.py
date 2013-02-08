#!/usr/bin/env python

import unittest
from listtree import ListTree
import functools

class ListTreeTest(unittest.TestCase):

    tree_layout = ['a','b','c',['a','b','c']]
    tree_layout_2 = ['a','b','c',['a','b','c',['a','b','c']]]
    tree_layout_3 = ['a','b','c', 1, 2, 3, ['a','b','c',['a','b','c']]]

    def testEquals(self):

        t1 = ListTree(value="Root Node", children=ListTreeTest.tree_layout)
        t2 = ListTree(value="Root Node", children=ListTreeTest.tree_layout)

        self.assertTrue(t1==t2)

        t1.value = "x"
        t2.value = "Y"
        self.assertFalse(t1==t2)

        t1.value = 15
        t2.value = 15
        self.assertTrue(t1==t2)
    
        t1 = ListTree(value="Root Node", children=ListTreeTest.tree_layout)
        t2 = ListTree(value="Root Node", children=ListTreeTest.tree_layout_2)
        self.assertFalse(t1==t2)

        t3_1 = ListTree(value=None, children=ListTreeTest.tree_layout_3)
        t3_2 = ListTree(value=None, children=ListTreeTest.tree_layout_3)
        self.assertTrue(t3_1==t3_2)

    def testLength(self):

        t1 = ListTree(value=None, children=ListTreeTest.tree_layout)
        t2 = ListTree(value=None, children=ListTreeTest.tree_layout_2)
        t3 = ListTree(value=None, children=ListTreeTest.tree_layout_3)

        self.assertTrue(len(t1) == 4)
        self.assertTrue(len(t2) == 4)
        self.assertTrue(len(t3) == 7)

    def testProperty(self):

        x = ListTree(value=None)
        self.assertTrue(x.value == None)

        x.value = 5
        self.assertTrue(x.value == 5)

    def testBasicIter(self):

        children = [4,5,6,'a','b','c']

        root = ListTree(value=None, children=children)
        result = [ y.value for y in root ]

        self.assertListEqual(children, result)

        result2 = [ y.value for y in root.children ]

        self.assertListEqual(children, result2)

    def testSlices(self):

        children = list(range(10))

        root = ListTree(children=children)
        root2 = [ ListTree(value = x) for x in children ]

        result = [ y.value for y in root.children ]
        self.assertListEqual(children, result)

        input1 = list(root[1:6])
        output1 = root2[1:6]
        self.assertListEqual(input1, output1)

        input1 = list(root[4:7])
        output1 = root2[4:7]
        self.assertListEqual(input1, output1)

        input1 = list(root[1:7])
        output1 = root2[4:7]
        self.assertNotEqual(input1, output1)
        
        input1 = list(root[1:5])
        output1 = root2[4:8]
        self.assertNotEqual(input1, output1)

        input1 = list(root[::-1])
        output1 = root2[::-1]
        self.assertListEqual(input1, output1)

        input1 = list(reversed(root))
        output1 = list(reversed(root2))
        self.assertListEqual(input1, output1)

    def testLoop(self):

        input1 = ListTree(children=ListTreeTest.tree_layout)
        input2 = ListTree(children=ListTreeTest.tree_layout_2)
        input3 = ListTree(children=ListTreeTest.tree_layout_3)

        self.assertFalse(input1.has_loop())
        self.assertFalse(input2.has_loop())
        self.assertFalse(input3.has_loop())

if __name__ == "__main__":

    unittest.main()
    

