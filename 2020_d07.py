import numpy as np
import pandas as pd
from pdb import set_trace
import re
from anytree import Node, RenderTree, PostOrderIter
from anytree import NodeMixin

class WNode(NodeMixin):
    def __init__(self, name, parent=None, weight=None, sum_weights=0):
        super(WNode, self).__init__()
        self.name = name
        self.parent = parent
        self.weight = weight# if parent is not None else None
        self.sum_weights = sum_weights# if parent is not None else None

    def _post_detach(self, parent):
        self.weight = None

def parse_input(filename):
    bags = {} 
    with open(filename, 'r') as f:
        for line in f:
            line = line.replace('bags', '').replace('bag', '')
            line = line.replace('.', '').replace(',', '')
            outer_key = '_'.join(line.split(' contain ')[0].split()[:2])
            bags[outer_key] = []
            items = line.split(' contain ')[1].split()
            for i in range(int(len(items)/3)):
                key = '_'.join(items[i*3+1:i*3+3] )
                val = int(items[i*3])
                d = {}
                d[key] = val 
                bags[outer_key].append(d)
    return bags

def construct_tree_pt1(data, curr_tree, root):
    for key, values in data.items():
        for v in values:
            if root in v:
                new_tree = WNode(key, parent=curr_tree)
                construct_tree_pt1(data, new_tree, key)
                break

def construct_tree_pt2(data, curr_tree, root):
    for key, values in data.items():
        if key == root:
            for v in values:
                for subkey, subvalue in v.items():
                    new_tree = WNode(subkey, parent=curr_tree, weight=subvalue)
                    construct_tree_pt2(data, new_tree, subkey)

def cal_bags(tree):
    for node in PostOrderIter(tree):
        if len(node.children) == 0:
            node.sum_weights = node.weight
        else:
            for i in range(len(node.children)):
                node.sum_weights += node.children[i].sum_weights
            node.sum_weights = node.sum_weights * node.weight + node.weight

if __name__ == '__main__':
    data = parse_input('data/2020_d07_input.txt')
    root_tree = WNode("shiny_gold", weight=1)
    construct_tree_pt2(data, root_tree, 'shiny_gold')
    all_nodes = set()
    cal_bags(root_tree)
    for pre, fill, node in RenderTree(root_tree):
        all_nodes.add(node.name)
        #print("%s%s" % (pre, node.name))
        print("%s%s (%s) (%s)" % (pre, node.name, node.weight or 0, node.sum_weights or 0))
    #print(all_nodes)
    #print(len(all_nodes)-1)
