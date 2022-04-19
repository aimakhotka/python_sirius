from platform import node


class Stack:
    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)
    def remove(self):
        return self.stack.pop()

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def remove(self):
        return self.queue.pop(0)

# stack = Stack()
# queue = Queue()
# for i in range(5):
#     queue.add(i)
# print(*queue.queue)
# print(queue.remove())
# print(*queue.queue)
    
class Deck:
    def __init__(self):
        self.deck = []
    
    def add(self, item, end=True):
        if end:
            self.deck.append(item)
        else:
            self.deck.insert(0, item)

    def remove(self, end=True):
        # if end:
        #     self.deck.pop()
        # else:
        #     self.deck.pop(0)
        return self.deck.pop() if end else self.deck.pop(0)

# deck = Deck()
# for i in range(3):
#     deck.add(i)
# print(deck.deck)
# for i in range(3, 6):
#     deck.add(i, end=False)
# print(deck.deck)

# print('Removed from end: ', deck.remove())
# print('After removal: ', deck.deck)
# print('Removed from start: ', deck.remove(False))
# print('After removal: ', deck.deck)

class Linked_Node:
    def __init__(self, value, next=None):
        self.value, self.next = value, next

    def add_next(self, next):
        self.next = next
    
    @classmethod
    def print_linked(cls, head):
        initial = head
        def rec_print(head):
            print(head.value)
            if head.next and head.next != initial:
                rec_print(head.next)
        rec_print(head)

# last_node = Linked_Node(3)
# head = Linked_Node(1, Linked_Node(2, last_node)) # 2 - tail
# other_node = Linked_Node(4, head)
# last_node.add_next(other_node)

# Linked_Node.print_linked(head)

class Double_Linked_Node(Linked_Node):
    def __init__(self, value, next=None, prev=None):
        self.value, self.next, self.prev = value, next, prev

    def add_next(self, next):
        self.next = next

    def add_prev(self, prev):
        self.prev = prev

# head = Double_Linked_Node(1)
# node_1 = Double_Linked_Node(2)
# node_2 = Double_Linked_Node(3)
# head.add_next(node_1)
# node_1.add_next(node_2)
# node_2.add_prev(node_1)
# node_1.add_prev(head)
# Double_Linked_Node.print_linked(head)




