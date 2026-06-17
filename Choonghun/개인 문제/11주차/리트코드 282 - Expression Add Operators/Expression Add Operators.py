class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        number = [[num[0]]]
        oper = []
        n = len(num)
        result = []
        def makeExpression():
            opers = ['+','-','*']
            operation = ''.join(number[0])
            for i in range(1, len(number)):
                idx = oper[i-1]
                nu = ''.join(number[i])
                operation = operation + opers[idx] + nu
            return operation

        def checkTarget():
            numStack = [int(''.join(number[0]))]
            if len(str(numStack[0])) != len(number[0]):
                return
            operStack = []
            for i in range(1, len(number)):
                itg = int(''.join(number[i]))
                if len(str(itg)) != len(number[i]):
                    return
                if oper[i-1] < 2:
                    numStack.append(itg)
                    operStack.append(oper[i-1])
                else:
                    numStack[-1] *= itg
            answer = numStack[0]
            for i in range(1,len(numStack)):
                if operStack[i-1]:
                    answer -= numStack[i]
                else:
                    answer += numStack[i]

            if answer == target:
                result.append(makeExpression())

        def backtrack(cur):
            if cur == n:
                checkTarget()
                return
            number.append([num[cur]])
            for i in range(3): # +, -, *, ''
                oper.append(i)
                backtrack(cur+1)
                oper.pop()
            number.pop()

            number[-1].append(num[cur])
            backtrack(cur+1)
            number[-1].pop()

        backtrack(1)
        return result