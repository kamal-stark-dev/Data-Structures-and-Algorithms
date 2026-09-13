"""
Union-Find / Disjoint Set Union (DSU) implementation.

Supports:
- Find                          O(α(n)) amortized
- Union                         O(α(n)) amortized
- Connected                     O(α(n)) amortized
- Component size                O(α(n)) amortized
- Number of components          O(1)

NOTE: α(n) is the inverse Ackermann function, which grows so slowly that for any practical input size, it is effectively constant time.

Optimizations:
- Path compression
- Union by size
"""

class UnionFind:

    def __init__(self, size=1):
        if size <= 0:
            raise RuntimeError("size must be greater than zero")

        self._size = size
        self.numComponents = size

         # Initially, every element is its own parent.
        self.id = list(range(size))

        # Initially, every component has size 1.
        self.sz = [1] * size

    def find(self, p: int) -> int:
        """Return the root of p and perform path compression."""

        if p < 0 or p >= self._size:
            raise IndexError("element out of range")

        root = p

        # Find the root.
        while root != self.id[root]:
            root = self.id[root]

        # compress the path leading back to the root (optimization)
        # this is called "path compression" and it gives amortized
        # constant time complexity.
        while p != root:
            next_node = self.id[p]
            self.id[p] = root
            p = next_node

        return root

        """
        # the iterative find function iterates from the root to parent
        # twice, once for finding the root and once for path compression
        # but it can all be done in a single iteration (recursively)

        if p != self.id[p]:
            self.id[p] = self.find(self.id[p])
        return self.id[p]
        """

    def connected(self, p: int, q: int) -> bool:
        """Return True if p and q belong to the same component."""

        return self.find(p) == self.find(q)

    def componentSize(self, p: int) -> int:
        """Return the size of the component containing p."""

        return self.sz[self.find(p)]

    def size(self) -> int:
        """Return the total number of elements."""

        return self._size

    def components(self) -> int:
        """Return the number of remaining components."""

        return self.numComponents

    def unify(self, p: int, q: int) -> None:
        """Merge the components containing p and q."""

        root1 = self.find(p)
        root2 = self.find(q)

        # Already in the same component/set.
        if root1 == root2:
            return

        # Union by size:
        # Attach the smaller tree to the larger tree.
        if self.sz[root1] < self.sz[root2]:
            root1, root2 = root2, root1

        self.id[root2] = root1
        self.sz[root1] += self.sz[root2]

        # since the roots found were different we know that
        # the number of components/sets has decreased by one
        self.numComponents -= 1


if __name__ == "__main__":
    uf = UnionFind(10)

    print("Initial number of components:", uf.components())

    # create some components
    uf.unify(0, 1)
    uf.unify(1, 2)

    uf.unify(3, 4)
    uf.unify(4, 5)

    uf.unify(6, 7)
    uf.unify(7, 8)

    print("\nUnified some elements.")

    print("\nNumber of components:", uf.components())

    # check connections
    print("0 and 2 connected:", uf.connected(0, 2))
    print("0 and 3 connected:", uf.connected(0, 3))
    print("3 and 5 connected:", uf.connected(3, 5))

    # component sizes
    print("size of component containing 0:", uf.componentSize(0))
    print("size of component containing 3:", uf.componentSize(3))
    print("size of component containing 9:", uf.componentSize(9))

    # merge two components
    uf.unify(2, 5)

    print("\nAfter unifying 2 and 5:")
    print("0 and 5 connected:", uf.connected(0, 5))
    print("Component size of 0:", uf.componentSize(0))
    print("Number of components:", uf.components())

    # display internal parent array
    print("\nParent array:", uf.id)
    print("Component sizes:", uf.sz)