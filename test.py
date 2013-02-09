#!/usr/bin/env python

import unittest
from tree import Tree
import functools

class TreeTest(unittest.TestCase):

    tree_layout = ['a','b','c',['a','b','c']]
    tree_layout_2 = ['a','b','c',['a','b','c',['a','b','c']]]
    tree_layout_3 = ['a','b','c', 1, 2, 3, ['a','b','c',['a','b','c']]]

    def testFlatIter(self):

        #Use value with defaulted paramaters
        t = Tree(value="Start", children=TreeTest.tree_layout)
        output = [ y for y in t.flat_value_iter() ]
        expected_result = [ "Start", 'a', 'b', 'c', 'a', 'b', 'c' ]
        self.assertEquals(output, expected_result)

        #Don't use value parameter
        t = Tree(children=TreeTest.tree_layout)
        output = [ y for y in t.flat_value_iter() ]
        expected_result = [ 'a', 'b', 'c', 'a', 'b', 'c' ]
        self.assertEquals(output, expected_result)

        #Don't use value, skip_none=False
        t = Tree(children=TreeTest.tree_layout)
        output = [ y for y in t.flat_value_iter(skip_none=False) ]
        expected_result = [ None, 'a', 'b', 'c', None, 'a', 'b', 'c' ]
        self.assertEquals(output, expected_result)


    def testEquals(self):

        t1 = Tree(value="Root Node", children=TreeTest.tree_layout)
        t2 = Tree(value="Root Node", children=TreeTest.tree_layout)

        self.assertTrue(t1==t2)

        t1.value = "x"
        t2.value = "Y"
        self.assertFalse(t1==t2)

        t1.value = 15
        t2.value = 15
        self.assertTrue(t1==t2)
        t1 = Tree(value="Root Node", children=TreeTest.tree_layout)
        t2 = Tree(value="Root Node", children=TreeTest.tree_layout_2)
        self.assertFalse(t1==t2)

        t3_1 = Tree(value=None, children=TreeTest.tree_layout_3)
        t3_2 = Tree(value=None, children=TreeTest.tree_layout_3)
        self.assertTrue(t3_1==t3_2)

    def testLength(self):

        t1 = Tree(value=None, children=TreeTest.tree_layout)
        t2 = Tree(value=None, children=TreeTest.tree_layout_2)
        t3 = Tree(value=None, children=TreeTest.tree_layout_3)

        self.assertTrue(len(t1) == 4)
        self.assertTrue(len(t2) == 4)
        self.assertTrue(len(t3) == 7)

    def testProperty(self):

        x = Tree(value=None)
        self.assertTrue(x.value == None)

        x.value = 5
        self.assertTrue(x.value == 5)

    def testBasicIter(self):

        children = [4,5,6,'a','b','c']

        root = Tree(value=None, children=children)
        result = [ y.value for y in root ]

        self.assertListEqual(children, result)

        result2 = [ y.value for y in root.children ]

        self.assertListEqual(children, result2)

    def testSlices(self):

        children = list(range(10))

        root = Tree(children=children)
        root2 = [ Tree(value = x) for x in children ]

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

        #No Loops

        input1 = Tree(children=TreeTest.tree_layout)
        input2 = Tree(children=TreeTest.tree_layout_2)
        input3 = Tree(children=TreeTest.tree_layout_3)

        self.assertFalse(input1.has_loop())
        self.assertFalse(input2.has_loop())
        self.assertFalse(input3.has_loop())

        input1.append(input2)

        self.assertFalse(input1.has_loop())

        #Loops

        input2.append(input1)
        input1.append(input2)

        self.assertTrue(input1.has_loop())

        input4 = Tree(children=TreeTest.tree_layout)
        input5 = Tree(children=TreeTest.tree_layout_2)
        input6 = Tree(children=TreeTest.tree_layout_3)

        input6.append(input4)
        input4.append(input5)
        input5.append(input6)

        self.assertTrue(input4.has_loop())
        self.assertTrue(input5.has_loop())
        self.assertTrue(input6.has_loop())


if __name__ == "__main__":

    unittest.main()


