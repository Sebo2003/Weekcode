class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None 

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def top(self):
        if not self.is_empty():
            return self.peek()
        else:
            return None
        
    def print(self):
        print("Stack:", self.items)
    
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = Stack()
        
        for i in range(len(game)):
            currElement = game[i]
            
            if currElement == 'C':
                stack.pop()
            elif currElement == 'D':
                top = stack.top()
                stack.push(int(top)*2)
            elif currElement == '+':
                top = stack.top()
                stack.pop()
                behind = stack.top()
                stack.push(int(top))
                stack.push(int(top)+int(behind))
            else:
                stack.push(currElement)

        stack.print()
        final = []

        if stack.is_empty() == False:
            while not stack.is_empty():
                final.append(int(stack.pop()))
            return sum(final)
        else:
            return 0
    
if __name__ == "__main__":
    sol = Solution()
    game = ["5","2","C","D","+"]
    score = sol.calPoints(game)
    print("GAME: ", game)
    print("SCORE: ", score)