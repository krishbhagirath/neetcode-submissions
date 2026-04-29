class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}

        # count frequencies in dictionary
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # sorted dictionary of (key, value) pairs (greatest to least)
        sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        result = [] # result list (will store the most frequent values)

        # take the k highest values
        for i in range(k):
            num, count = sorted_items[i] # stores the key in num, value in count, for the sorted dictionary at index i
            result.append(num)  # add values to list
        
        return result # return / print