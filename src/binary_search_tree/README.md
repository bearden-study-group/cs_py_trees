# Intro to Binary Search Trees

To understand Binary Search Trees, it might be helpful to first understand Binary Trees (without the Search part). And
to understand Binary Trees, we should probably understand Trees (without the Binary part).

## Trees

In computer science, a `tree` is a widely used abstract data type (ADT) that simulates a hierarchical tree structure,
with a root value and subtrees of children with a parent node, often represented as a set of linked nodes.

A tree data structure can be defined recursively as a collection of nodes (starting at the root node), where each node
is a data structure consisting of a `valeu`, together with a list of references to `nodes` (the "children"), with the
constraints that no reference is duplicated, and none points to the root.

Alternatively, a tree can be defined abstractly as a whole (globally) as an `ordered tree`, with a value assigned to
each node. Both of these perspectives are useful: while a tree can be analyzed mathematically as a whole, when actually
represented as a data structure it is usually represented and worked with separately by node (rather than a set of nodes
and an adjacency list of edges between nodes, as one may represent in a digraph, for instance). For example, looking at
a tree as a whole, one can talk about the "parent node" of a given node, but in general, as a data structure, a given
node only contains the list of its children but does not contain a reference to its parents (if any).

![Generic Non-Binary Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Tree_%28computer_science%29.svg/220px-Tree_%28computer_science%29.svg.png)

Here we have a generic (and so non-binary), unsorted, some-labels-duplicated, arbitrary diagram of a tree. In this
diagram, the node labeled 7 has three children (labeled 2, 10, 5, and one parent, labeled 2).

Now. Stop and think about how you might represent this in a class form. Should we have one big `Tree` class that holds a
bunch of nodes? Should we have a `Node` class? What would that `Node` class look like—what properties would that have?

#### Some Possibilities

<details>
<summary>Click to expand!</summary>

### `Node` — A Class Representation of a Tree

- `value`  — The value to store. This will for sure be included in our solution
- `children`  — We could store a list of children Nodes. Can be of any length for generic tree.
    - `children = [Node("B"), Node("C")`
- `parent_node` — We COULD store a reference to the Parent Node for convenience (like doubly-linked-list)

### `Tree` — A Class Representation of a Tree

- `root_node` — We could keep track of the root node at all times. <br>
    - `root_node = None` if the Tree is empty (thus there IS NO root node)
    - OR `root_node = Node(X)` if there's at least one node in list
- `nodes` — We COULD store all the nodes inside this container...

```python

class Node:
    def __init__(self, value):
        # the new_value this node is storing  
        self.value = value

        # literally store references to EVERY CHILD that the Node has
        self.children = []  # [Node("B"), Node("C")]  if we're in Node("A")

        # we could store a reference to the parent 
        # (i.e., None if root node, else the parent node.) 
        self.parent = None


class Tree:
    def __init__(self):
        # point at the root node in tree. (or None if tree is empty)  
        self.root_node = None  # or Node("A") if node A was root

        # literally store every node in the tree in some container (like list)
        self.nodes = []  # or [Node("A"), Node("B"), Node("C")] if we had nodes A, B, C 

        # we could track size if we wanted to
        self.size = 0  # or 3 if we had nodes A, B, C
```

- `nodes = [Node(A), Node(B), Node(C)]`  for three nodes with values A, B, and C respectively
- `nodes = []` if there are no nodes.
- <strong>NOTE:</strong> If we have a list collecting nodes, should we have a `Node` class that tracks connections?

- `size`

</details>

So. When thinking about how trees might work, let's think to what we did

## Binary Trees

## Binary Search Trees
