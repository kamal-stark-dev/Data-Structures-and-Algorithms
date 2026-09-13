class DisjoinSetUnion:
    def __init__(self, n: int):
        self.Parent = list(range(n))
        self.Size = [1] * n

    def find(self, node: int) -> int:
        if self.Parent[node] != node:
            # path compression + parent finding
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, node1: int, node2: int) -> bool:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2: # already in the same set
            return False

        if self.Size[root1] < self.Size[root2]:
            root1, root2 = root2, root1

        self.Parent[root2] = root1
        self.Size[root1] += self.Size[root2]

        return True