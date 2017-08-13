class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operand, operator, num, res = [], [], '', 0

        for i in s:
            if i.isdigit():
                num += i
            else:
                if num:
                    operand.append(num)
                num = ''
                if i == '+' or i == '-' or i == '(':
                    operator.append(i)
                if i == ')':
                    while operator[-1] != '(':
                        if operator.pop() == '+':
                            if operator and operator[-1] == '-':
                                operand.append(-int(operand.pop()) + int(operand.pop()))
                            else:
                                operand.append(int(operand.pop()) + int(operand.pop()))
                        else:
                            if operator and operator[-1] == '-':
                                operand.append(int(operand.pop()) + int(operand.pop()))
                                operator[-1] == '-'
                            else:
                                operand.append(-int(operand.pop()) + int(operand.pop()))
                    operator.pop()
        if num: operand.append(num)


        while operator:
            if operator.pop() == '+':
                if operator and operator[-1] == '-':
                    operand.append(-int(operand.pop()) + int(operand.pop()))
                else:
                    operand.append(int(operand.pop()) + int(operand.pop()))
            else:
                 if operator and operator[-1] == '-':
                    operand.append(int(operand.pop()) + int(operand.pop()))
                    operator[-1] == '-'
                 else:
                    operand.append(-int(operand.pop()) + int(operand.pop()))


        return int(operand[-1])


o = Solution()
print o.calculate("(1+(4+5+2)-13)+(6+8)")