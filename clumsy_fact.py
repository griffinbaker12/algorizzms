class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = [n]
        operation_cnt = 0
        for i in range(n - 1, 0, -1):
            if operation_cnt % 4 == 0 or operation_cnt % 4 == 1:
                if operation_cnt % 4 == 0:
                    stack[-1] *= i
                else:
                    # because it gets fucked up with negatives...
                    stack[-1] = int(stack[-1] / i)
            else:
                stack.append(i) if operation_cnt % 4 == 2 else stack.append(-i)
            operation_cnt += 1

            print(stack)

        # combine_vals
        return sum(stack)


sol = Solution()
print(sol.clumsy(10))
