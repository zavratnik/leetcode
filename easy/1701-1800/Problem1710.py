from typing import List

class Problem1710:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort po units v padajočem vrstnem redu
        boxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        ans = 0

        for count, units in boxes:
            if truckSize == 0:
                break

            take = min(count, truckSize)
            ans += take * units
            truckSize -= take

        return ans


if __name__ == "__main__":
    solution = Problem1710()
    print(solution.maximumUnits([[1,3],[2,2],[3,1]], 4))     # 8
    print(solution.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))  # 91
