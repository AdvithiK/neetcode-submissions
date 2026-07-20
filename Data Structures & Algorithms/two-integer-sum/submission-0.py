class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make a hashmap of nums -> val : index
        hmap = {} 
        
        for i,nval in enumerate(nums):
            #find the difference
            goal_val = target - nval
            #check if it's in the hashmap, if not add it 
            if goal_val in hmap:
                return [hmap[goal_val], i]
            #update hashmap
            hmap[nval] = i
        return 
        