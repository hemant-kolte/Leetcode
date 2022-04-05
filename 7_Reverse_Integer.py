
class Solution:
    def reverse(self, x: int):
        res, isPos = 0, 1
        if x < 0:
            isPos = -1
            x = -1 * x
        while x != 0:
            res = (res * 10) + (x % 10)
            if res > 2147483647:
                return 0
            self.method(x)
        return (res * isPos)

    def method(self, x):
        x = int(x/10)
if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))