class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {} # 1 - new freq dict, create freq table

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        # num (1,2,3,etc) = keys
        # count = values

        # next - sort the values of the dict (freq)
        sorted_nums = sorted(freq, key=freq.get, reverse=True) # 2 - sort based on frequencies
            # sorted (what is being sorted, what is being used to sort, reverse or  not)
            # Freq.get POINTS TO THE VALUES (FREQUENCIES)
            # the keys (numbers) get sorted BASED on the key in sorted(), which is the values       (frequencies)

            # returns a single list

        
        count = 0
        numbers = [] # 3 - initialize new array, loop until k, append k numbers, return

        # loop through while count < k
        while count < k:
            numbers.append(sorted_nums[count])
            count += 1


        return numbers



# Steps:
# 1) freq table
# 2) sort based on frequencies
# 3) loop through new list, append up to k values, and return



























        # frequency = {}

        # # count frequencies in dictionary
        # for num in nums:
        #     frequency[num] = frequency.get(num, 0) + 1

        # # sorted dictionary of (key, value) pairs (greatest to least)
        # sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        # result = [] # result list (will store the most frequent values)

        # # take the k highest values
        # for i in range(k):
        #     num, count = sorted_items[i] # stores the key in num, value in count, for the sorted dictionary at index i
        #     result.append(num)  # add values to list
        
        # return result # return / print