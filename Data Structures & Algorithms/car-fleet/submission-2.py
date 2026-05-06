class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        cars.sort(reverse=True)

        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


# Algorithm:
# - sort the position array in descending order (higher positions first, lower later)
# - loop over every (pos, spd) pair, calculate time
# 	- each time, check:
# 		- if stack is empty OR the current time is greater than the one at the top of the stack
# 		- append to stack (i.e. created a new fleet, will not merge)
# 		- if current time is less than or equal to the last value, that means they will merge at some point (i.e. not a separate fleet)