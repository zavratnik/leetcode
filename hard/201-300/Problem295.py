import heapq


class Problem295:
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
            if len(self.left) > len(self.right) + 1:
                val = -heapq.heappop(self.left)
                heapq.heappush(self.right, val)

        else:
            heapq.heappush(self.right, num)
            if len(self.right) > len(self.left):
                val = heapq.heappop(self.right)
                heapq.heappush(self.left, -val)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2


if __name__ == "__main__":
    mf = Problem295()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # 1.5
    mf.addNum(3)
    print(mf.findMedian())  # 2
