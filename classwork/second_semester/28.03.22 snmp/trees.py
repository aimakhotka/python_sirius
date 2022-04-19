from tkinter.tix import Tree


class Tree_node:
    def __init__(self, value, nodes=[]):
        self.value, self.nodes = value, nodes

    def add_node(self, node):
        self.links.append(node)

    @classmethod
    def print_tree_depth(cls, head):
        print(head.value)
        for node in head.nodes:
            cls.print_tree_depth(node)

    @classmethod
    def print_tree_breadth(cls, head):
        visited = []
        def bfs(head, visited, queue):
            visited.append(head)
            queue.append(head)
            while queue:
                next = queue.pop(0)
                for node in next.nodes:
                    if node not in visited:
                        visited.append(node)
                        queue.append(node)

        bfs(head, visited, queue=[])
        [print(node.value) for node in visited]

head = Tree_node(1, [Tree_node(i,\
    [Tree_node(j * i) for j in range(5, 8)]) for i in range(2,5)])

print('Depth: ')
Tree_node.print_tree_depth(head)
print('-'*100, '\nBredth: ')
Tree_node.print_tree_breadth(head)
