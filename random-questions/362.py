from collections import deque

class HitCounter:

    def __init__(self):
        self.hitcount = 0
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        self.hitcount += 1

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp-300:
            self.hits.popleft()
            self.hitcount -= 1
        return self.hitcount if self.hitcount > 0 else 0


# Your HitCounter object will be instantiated and called as such:
obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
obj.hit(300)
obj.hit(300)
obj.hit(301)
param_2 = obj.getHits(301)

# Results:  53.28% time (34ms) 49.38% space (14MB)