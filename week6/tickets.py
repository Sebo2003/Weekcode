class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def print(self):
        print("Queue: ", self.items)

class Solution:
    def timeRequiredToBuy(self, tickets, k):
        queue = Queue()
        for i, t in enumerate(tickets):
            queue.enqueue((i, t))
        
        time = 0
        while not queue.is_empty():
            idx, remaining = queue.dequeue()
            buy = min(remaining, 1)
            remaining -= buy
            time += buy
            
            if idx == k:
                if remaining == 0:
                    return time
                else:
                    queue.enqueue((idx, remaining))
            else:
                queue.enqueue((idx, remaining))

        return time

if __name__ == "__main__":
    tickets1 = [2, 3, 2]
    k1 = 2
    sol = Solution()
    print(sol.timeRequiredToBuy(tickets1, k1))  

    tickets2 = [5, 1, 1, 1]
    k2 = 0
    print(sol.timeRequiredToBuy(tickets2, k2))