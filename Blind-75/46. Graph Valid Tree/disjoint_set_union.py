class DisjointSetUnion:
    def __init__(self, size):
        if size <= 0:
            raise RuntimeError("size must be greater than zero")

        self.components = size
        self.Parent = list(range(size))
        self.Size = [1] * size

    def find(self, node: int) -> int:
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])

        return self.Parent[node]

    def union(self, node1: int, node2: int) -> bool:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False

        if self.Size[root1] < self.Size[root2]:
            root1, root2 = root2, root1

        self.Parent[root2] = root1
        self.Size[root1] += self.Size[root2]

        self.components -= 1

        return True

    def getComponentCount(self) -> int:
        return self.components