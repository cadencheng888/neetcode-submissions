class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        mydict = {}
        for num in nums:
            if num not in mydict:
                mydict[num] = 1
            else:
                mydict[num] += 1
        sorted_items = sorted(mydict.items(), key = lambda item: item[1], reverse = True)
        for i in range(k):
            result.append(sorted_items[i][0])
        return result
        
            