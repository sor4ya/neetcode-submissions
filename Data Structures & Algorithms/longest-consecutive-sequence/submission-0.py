class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        length, max_length = 0,0

        for n in seen:
            if n - 1 in seen:
                # if the previous element before this is in set 
                # continue till you hit that min of this sequence
                continue
            length = 0

            while (n + length) in seen:
                length += 1
            max_length = max(max_length, length)

        return max_length


