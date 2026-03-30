class MinStack:

    def __init__(self):
        self.main_stack = []
        self.support_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.support_stack:
            self.support_stack.append(val)
        else:
            if self.support_stack[-1] >= val:
                self.support_stack.append(val)

    def pop(self) -> None:
        pop_val = self.main_stack.pop()
        if self.support_stack and pop_val == self.support_stack[-1]:
            self.support_stack.pop()
        
    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.support_stack[-1]
        
