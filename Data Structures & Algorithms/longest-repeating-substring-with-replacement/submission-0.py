class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window using L & R

        res = 0
        #hashmap to store the count of letters
        count = {}

        l, max_f = 0,0
        #move r until window - max freq < k
        for r in range(len(s)):
            #update the letter count in hashmap
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(max_f, count[s[r]])

            #slide r & decrement count
            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res




        