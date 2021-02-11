# AVL Trees

## Time Complexity in Big O Notation

| Algorithm | Average    | Worst-Case |
|-----------|------------|------------|
| Space     | `O(n)`     | `O(n)`     |
| Search    | `O(log n)` | `O(log n)` |
| Insert    | `O(log n)` | `O(log n)` |
| Delete    | `O(log n)` | `O(log n)` |

## Animation

Animation showing the insertion of several elements into an AVL tree. It includes left, right, left-right, and
right-left rotations.

![Depiction of AVL Tree](https://upload.wikimedia.org/wikipedia/commons/f/fd/AVL_Tree_Example.gif)

An _AVL Tree_ (named after the inventors Adelson-Velsky and Landis) is a self-balancing binary search tree. It was the
first such data structure to be in invented (in 1962). In an AVL tree, the heights of the two child subtrees of any node
differ by at most one; if at any time they differ by MORE THAN ONE, rebalancing is done to restore this property.
Lookup, insertion, and deletion all take O(log n) time in both the average case and worst case, where `n` is the number
of nodes in the tree PRIOR TO the operation.

Insertions and deletions may require the tree to be rebalanced by one or more tree rotations.

AVL trees are often compared with red-black trees because both support the same set of operations and take O(log n) time
for the basic operations.

For lookup-intensive applications, AVL Trees are FASTER THAN red-black trees because they are more strictly balanced.

Similar to red-black trees, AVL trees are height-balanced. Both are, in general, neither weight-balanced nor 𝜇-balanced
for any 𝜇 ≤ 1/2. In human: sibling nodes can have hugely differing numbers of descendants.

## Definition (Math and shit!)

In a binary tree, the balance factor of a node X is defined to be the height difference of its two child sub-trees.

```
BalanceFactor(NodeX) := Height(RightSubtree(NodeX)) - Height(LeftSubtree(NodeX))
```

A binary tree is defined to be an AVL tree if the invariant holds for every node X in the tree.

```
BalanceFactor(NodeX) ∈ {-1, 0, 1} 
# so, BalanceFactor(NodeX) is -1 or 0 or 1
```

A node X with BF(X) < 0 is called "left-heavy", one with BF(X) > 0 is called "right-heavy", and one with BF(X) = 0 is
sometimes simply called "balance".

## Operations

Read-only operations of an AVL tree involve carrying out the same actions as would be carried out on an unbalanced
binary search tree, but modifications have to observe and restore the height balance of sub-trees.

### Searching

Searching for a specific key in an AVL tree can be done in the same way as that of any balanced or unbalanced binary
tree. In order for search to work effectively, it has to employ a comparison function which establishes total order (or
at least total pre-order) on the set of keys. The number of comparisons required for successful search is limited by the
height `h` and for unsuccessful search is very close to `h`, so both are in `O(log n)`.

### Traversal

As a read only operation the traversal of an AVL tree functions the same way as on ony other binary tree. Exploring
all `n` nodes of the tree visits each link exactly twice: one downward visit to enter the subtree rooted by that node,
another visit upward to leave that node's subtree after having explored it.

Once a node has been found in an AVL tree, the `next` or `previous`  node can be accessed in amortized constant time. 