class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value = arrays[0][0]
        max_value = arrays[0][-1]

        max_distance = 0

        for array in arrays[1:]:
            # Update max_distance
            max_distance = max(max_distance, abs(array[0] - max_value), abs(array[-1] - min_value))

            # Update min and max values for subsequent iterations
            min_value = min(min_value, array[0])
            max_value = max(max_value, array[-1])

        return max_distance