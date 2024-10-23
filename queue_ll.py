class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"Node {self.value}"


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, n):
        if not self.head or not self.tail:
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def dequeue(self):
        if not self.head:
            self.tail = None
            return None
        old_head = self.head
        self.head = old_head.next
        return old_head

    def __str__(self):
        nodes = []
        curr_node = self.head
        while curr_node:
            nodes.append(str(curr_node))
            curr_node = curr_node.next
        return "The queue is: " + ", ".join(nodes)


nodes = [Node(i) for i in range(1, 6)]
q = Queue()

for n in nodes:
    q.enqueue(n)
print(q)

while n := q.dequeue():
    print(n)
