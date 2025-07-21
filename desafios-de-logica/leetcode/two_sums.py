class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for idx, x in enumerate(nums):
            if store.get(x) is not None:
                return [store.get(x), idx]

            store.update({target-x: idx})

