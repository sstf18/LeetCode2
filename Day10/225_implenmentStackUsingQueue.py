

from collections import deque


class myStack: 
    def __init__(self) -> None:
        self.que = deque()

    def push(self, x: int) -> None: 
        self.que.append(x)
    
    def pop(self) -> int: 
        if self.empty():
            return None
        for _ in range(len(self.que)-1): # mins '1', since they need to keep the last one element in orginal
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int: 
        if self.empty():
            return None
        return self.que[-1]

    def empty(self) -> bool: 
        return not self.que