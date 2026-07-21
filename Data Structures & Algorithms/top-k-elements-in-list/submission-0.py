class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a list of nums size: max amount of times a val can appear
        arr = [[] for i in range(len(nums) + 1)]

        #hashmap to store the occurances of each value
        hmap = {} #val: occurances
        #loop through the array and populate hashmap 
        for i in nums:
            hmap[i] = hmap.get(i,0) + 1
        #store the number at the count it occurs in arr
        for num, count in hmap.items():
            arr[count].append(num)
        
        res = []
        #go through the array from back -> front and return k most freq nums
        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res

        