class Problem981:
    def __init__(self):
        self.timestamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamp:
            self.timestamp[key] = []

        self.timestamp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp:
            return ""

        arr = self.timestamp[key]
        left = 0
        right = len(arr) - 1

        # če je iskani timestamp po zadnjem znanem, vrni zadnjo vrednost
        if timestamp >= arr[right][0]:
            return arr[right][1]

        # binary search za prvi timestamp > iskani
        while left < right:
            mid = left + (right - left) // 2

            if timestamp >= arr[mid][0]:
                left = mid + 1
            else:
                right = mid

        # right je prvi timestamp > iskani
        return "" if right == 0 else arr[right - 1][1]


if __name__ == "__main__":
    kv = Problem981()
    kv.set("foo", "bar", 1)
    print(kv.get("foo", 1))   # "bar"
    print(kv.get("foo", 3))   # "bar"
    kv.set("foo", "bar2", 4)
    print(kv.get("foo", 4))   # "bar2"
    print(kv.get("foo", 5))   # "bar2"
