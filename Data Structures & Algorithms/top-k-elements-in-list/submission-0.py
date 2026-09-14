class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []
        i = 0

        while i < k:
            if counts:
                max_key = max(counts, key=counts.get)
                del counts[max_key]
                res.append(max_key)
                i += 1
            else: 
                break
        return res