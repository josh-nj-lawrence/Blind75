from collections import deque

class Logger:
    def __init__(self):
        self._queue = deque() # Queue for incoming messages, only print when queue is not null
        self._msg_set = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self._queue:
            msg, ts = self._queue[0]
            if timestamp - ts >= 10:
                self._queue.popleft()
                self._msg_set.remove(msg)
            else:
                break
        if message not in self._msg_set:
            self._msg_set.add(message)
            self._queue.append((message, timestamp))
            return True
        else:
            return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message).

# Results: 17.85% time (157ms) 25.6% space (20.8MB)