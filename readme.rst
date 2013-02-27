TreePy
======

A Tree implementation in python

The Tree class is the node type that looks like this:

 * tree.value:  Holds a particular value
 * tree.children:  A list to the children

Each node can be treated like a list in that it supports the following
functions:

 * tree.append()

Also slices are supported:

 * [0-4]

 * [::-1]

To iterate over all the values of the tree or subtree use:

 * tree.flat_value_iter()

To iterate over all the nodes of the subtree use:

 * tree.flat_node_iter()

Otherwise the iterator and returns a tree object rather than the value.

.. code-block:: python

    t = Tree(children=[1,2,3])

    try:
        while True:
            i = iter(t)
            node = i.next()
            print node.value
    except StopIteration:
        pass

