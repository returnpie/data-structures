class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

def dfs_with_recursion(node):

    node.visited = True
    print(node.name)

    for n in node.adjacency_list:
        if not n.visited:
            dfs_with_recursion(n)

if __name__ == "__main__":

    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    dfs_with_recursion(node1)