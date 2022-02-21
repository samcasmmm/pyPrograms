stack = []


def push(self, n):
    self.append(n)


def pop(n):
    if len(stack) == 0:
        print('Stack is Empty')
        return False
    else:
        stack.pop()
        return stack