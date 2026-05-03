class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]

        stack = [] 
        result = [0] * len(temperatures) # indices of temperatures

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[(stack[-1])]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            
            stack.append(i)
        
        return result
