class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, operator, num = [], [], ''
        for i in s:
            if i == ' ': continue
            if i.isdigit():
                num += i
            else:
                if num:
                    if not stack: stack.append(int(num))
                    else:
                        if stack and stack[-1] == '*':
                            stack.pop()
                            stack.append(int(num) * stack.pop())
                        elif stack and stack[-1] == '/':
                            stack.pop()
                            stack.append(stack.pop() / int(num))
                        else:
                            stack.append(int(num))
                    num = ''

                if i == '*' or i == '/':
                    stack.append(i)
                if i == '+' or i == '-':
                    operator.append(i)


        if num and stack:
            sigh = stack[-1]
            if sigh == '*':
                stack.pop()
                stack.append(int(num) * stack.pop())
            elif sigh == '/':
                stack.pop()
                stack.append(stack.pop() / int(num))
            else:
                stack.append(int(num))
            num = ''
        if not stack and num:
            return int(num)



        while operator:
            first_op = operator.pop()
            if not operator:
                stack.append(stack.pop() + stack.pop()) if first_op == '+' else stack.append(- stack.pop() + stack.pop())
            else:
                if first_op == '+' and operator[-1] == '+' or first_op == '-' and operator[-1] == '-':
                    stack.append(stack.pop() + stack.pop()) if first_op == '+' else stack.append(stack.pop() + stack.pop())
                if first_op == '+' and operator[-1] == '-' or first_op == '-' and operator[-1] == '+':
                    stack.append(- stack.pop() + stack.pop())
        return stack[-1]
o = Solution()
print o.calculate('0*1')