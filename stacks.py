from node import Node


class Stack:
    def __init__(self):
        self.top_item = None
        pass

    def peek(self):
        return self.top_item.value
