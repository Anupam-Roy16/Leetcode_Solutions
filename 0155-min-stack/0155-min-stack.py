class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, val: int) -> None:
        self.stack1.append(val)
        if len(self.stack2) == 0:
            self.stack2.append(val)
        else:
            if self.stack2[len(self.stack2)-1]>=val:
                self.stack2.append(val)

    def pop(self) -> None:
        temp = self.stack1.pop()
        if temp == self.stack2[len(self.stack2)-1]:
            self.stack2.pop()

    def top(self) -> int:
        return self.stack1[len(self.stack1)-1]
        

    def getMin(self) -> int:
        return self.stack2[len(self.stack2)-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()