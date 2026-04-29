class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opStack = []

        for element in tokens:
            if(element == '+' or element == '-' or element == '*' or element == '/'):
                newVal = 0
                right = int(opStack.pop())
                left = int(opStack.pop())
                if(element == '+'):
                    newVal = left + right
                elif(element == '-'):
                    newVal = left - right
                elif(element == '*'):
                    newVal = left * right
                elif(element == '/'):
                    newVal = left / right

                opStack.append(int(newVal))

            else:
                opStack.append(int(element))

        
        return opStack[0]