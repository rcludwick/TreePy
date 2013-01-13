import unittest
from tree import Tree
import functools

class TreeTest(unittest.TestCase):

    tree_layout = ['a','b','c',['a','b','c']]
    tree_layout_2 = ['a','b','c',['a','b','c',['a','b','c']]]
    tree_layout_3 = ['a','b','c', 1, 2, 3, ['a','b','c',['a','b','c']]]

    def testEquals(self):

        t1 = Tree(value="Root Node", children=TreeTest.tree_layout)
        t2 = Tree(value="Root Node", children=TreeTest.tree_layout)

        self.assertTrue(t1==t2)

        t1.value = "x"
        t2.value = "Y"
        self.assertTrue(t1==t2)

        t1.value = 15
        t2.value = 15
        self.assertTrue(t1==t2)
    
        t1 = Tree(value="Root Node", children=TreeTest.tree_layout)
        t2 = Tree(value="Root Node", children=TreeTest.tree_layout_2)

        #Fails for now
        self.assertFalse(t1==t2)


    def testLength(self):

        t1 = Tree(value=None, children=TreeTest.tree_layout)
        t2 = Tree(value=None, children=TreeTest.tree_layout_2)
        t3 = Tree(value=None, children=TreeTest.tree_layout_3)

        self.assertTrue(len(t1) == 0)
        self.assertTrue(len(t1) == 4)
        self.assertTrue(len(t2) == 4)
        self.assertTrue(len(t3) == 7)


        






if __name__ == "__main__":

    unittest.main()
    

