class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for num, count in count.items():
            freq[count].append(num)
        result = []
        print(len(freq))
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                print(i, n)
                result.append(n)
                if len(result) == k:
                    return result