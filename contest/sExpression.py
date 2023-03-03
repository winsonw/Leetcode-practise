#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'sExpression' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING nodes as parameter.
#
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.child = []
        
    def add_child(self, node):
        self.child.append(node)
        if len(self.child) == 2:
            if node.value == self.child[0].value:
                raise Exception("E2")
            if self.child[0].value > self.child[1].value:
                self.child[0], self.child[1] = self.child[1], self.child[0]
        elif len(self.child) > 2:
            for c in self.child:
                if c.value == node.value:
                    raise Exception("E2")
            raise Exception("E1")
        
    def attach_root(self, node):
        if self.parent:
            print(self.value)
            print(node.value)
            print(self.parent.value)
            raise Exception("E4")
        self.parent = node

def sExpression(nodes):
    # Write your code here
    def read_input(nodes):
        dependence = []
        root = None
        for c in nodes:
            if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if not root:
                    root = c
                else:
                    dependence.append([root, c])
                    root = None
                    
        return dependence
    
    dependence = read_input(nodes)
    
    def form_tree(dependence):
        collections = {}
        for r, l in dependence:
            if not r in collections:
                collections[r] = TreeNode(r)
            if not l in collections:
                collections[l] = TreeNode(l)

            print(r,l)
            collections[r].attach_root(collections[l])
            collections[l].add_child(collections[r])
            
        roots = []
        for key in collections:
            if not collections[key].parent:
                roots.append(collections[key])
            
        if len(roots) == 0:
            raise Exception("E3")
        if len(roots) > 1:
            print('me?')
            raise Exception("E4")
        
        return roots[0]
    
    root = form_tree(dependence)
        
        
    # def print_tree(node):
    #     print('('+node.value,end='')
    #     if node.child:
    #         for c in node.child:
    #             print_tree(c)
    #     print(')',end='')
    s = ''
    def print_tree(node):
        s = s + '('+ node.value
        if node.child:
            for c in node.child:
                print_tree(c)
        s = s + ')'
        
    print_tree(root)
                
    
                    

if __name__ == '__main__':

    nodes = "(B,D) (D,E) (A,B) (C,F) (E,G) (A,C)"

    result = sExpression(nodes)

    fptr.write(result + '\n')

    fptr.close()
