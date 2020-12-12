"""
Tree Node
----------

This node represents an item in the tree. Each node contains its key as well as
the value of the subtree rooted at this node. It supports operations to add
children, as well as check if this is a leaf or not.
"""

class Node:
    """
    Node Class
    - Init: Sets the basic information such as the key, children, and value of
    subtree.
    - add_child(child_node): Adds the child node to the list of children.
    - is_external(): Checks if the node is a leaf.
    - children(): returns the list of children.
    """


    def __init__(self, key, parent=None):
        """
        The initialisation of the node sets the key and instantiates the
        children (as empty).
        :param key: The value of the node.
        :param parent: The parent of the node.
        """
        self.key = key
        self.parent = parent
        self.subtree_value = key
        self.children = []
        self.sum_of_children = 0;




    def get_subtree(self):
        return self.subtree_value


    def find_subtree(self):
        i = 0
        largest = 0
        # self.subtree_value = 0
        while (i < len(self.children)):
            if(self.children[i].subtree_value > largest):

                largest = self.children[i].subtree_value

            i+=1

        if(largest < self.subtree_value):
            self.subtree_value = self.key
        else:
            self.subtree_value = largest






    def add_child(self, child_node):
        """
        Adds `child_node` as a child of this node. Adds to the list of children
        and performs required calculations.
        :param child_node: The child node to add (class Node)
        """

        self.children.append(child_node)
        self.find_subtree()

        # self.subtree_up(child_node)


    def is_external(self):
        """
        Checks if the node is a leaf node in the tree.
        :return: Boolean, True if leaf, False otherwise.
        """
        if (len(self.children)==0):
            return True

        return False

    def get_parent(self):
        return self.parent

    def find_remove(self,node):
        for  i in self.children:
            if (i == node):
                self.children.remove(node)
                return
            else:
                return







    def get_children(self):
        """
        Returns the children of the current node.
        :return: List of children.
        """


        return self.children
        # Can also access this using "node.children", but putting
        # this here for ease of use and standard usage things in
        # other languages people might be used to.
