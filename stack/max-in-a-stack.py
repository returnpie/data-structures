# LIFO: last item insert is the first item we take out


class Stack:

    def __init__(self):
        self.main_stack = []

        self.max_stack = []

    # insert item into the stack // O(1)

    def push(self, data):
        self.main_stack.append(data)

        if len(self.main_stack) == 1:
            self.max_stack.append(data)
            return

        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    # remove and return the last item we have inserted (LIFO) // O(1)
    def pop(self):
        if self.stack_size() < 1:
            return -1

        self.max_stack.pop()
        return self.main_stack.pop()

    def get_max_item(self):
        return self.max_stack.pop()


stack = Stack()
stack.push(1000)
stack.push(5)
stack.push(1)
stack.push(12)
stack.push(100)

print(stack.get_max_item())
