from typing import List


class Problem321:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans: List[int] = []

        def max_subsequence(nums: List[int], t: int) -> List[int]:
            stack: List[int] = []
            drop = len(nums) - t

            for num in nums:
                while stack and stack[-1] < num and drop > 0:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            return stack[:t]

        def merge_max(seq1: List[int], seq2: List[int]) -> List[int]:
            merge: List[int] = []
            i = 0
            j = 0

            while i < len(seq1) or j < len(seq2):
                if i == len(seq1):
                    merge.extend(seq2[j:])
                    break
                elif j == len(seq2):
                    merge.extend(seq1[i:])
                    break
                else:
                    if seq1[i:] > seq2[j:]:
                        merge.append(seq1[i])
                        i += 1
                    else:
                        merge.append(seq2[j])
                        j += 1
            return merge

        for t in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            sub1 = max_subsequence(nums1, t)
            sub2 = max_subsequence(nums2, k - t)

            temp = merge_max(sub1, sub2)
            ans = max(ans, temp)

        return ans


if __name__ == "__main__":
    solution = Problem321()
    print(solution.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))  # [9, 8, 6, 5, 3]
    print(solution.maxNumber([6, 7], [6, 0, 4], 5))                 # [6, 7, 6, 0, 4]
    print(solution.maxNumber([3, 9], [8, 9], 3))                    # [9, 8, 9]
